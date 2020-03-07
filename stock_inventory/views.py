import csv
import MySQLdb
import pandas as pd
import pytz
import datetime
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage

from stock_inventory.forms import Dropdown
from backend.stamp_backend import process_purchases, process_sales, get_obj, stamp_verifier, puchase_insert, stamp_sold
from backend.config import stamp_types, stamp_table_and_denomination

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Dropdown(request.POST)
        if form.is_valid():
            table_name = form['category'].value()
            if table_name == 'select':
                return render(request, 'home.html', {'form': form, 'form_invalid': True})
            obj = get_obj(table_name)
            denomination = 0
            extra_col = False
            for key in stamp_types:
                if key == table_name:
                    denomination = stamp_types[key]
                    if "sale" in request.POST:
                        data = obj.objects.filter(is_sale=1, delete_flag=0)
                        extra_col = True
                    else:
                        data = obj.objects.filter(is_sale=0, delete_flag=0)
            return render(request, 'home.html', {'datas': data, 'denomination':denomination, 'extra':extra_col, 'data':True})
    else:
        form = Dropdown()
    return render(request, 'home.html', {'form': form, 'data':False})


def purchase_upload(request):
    purchase_document_path = f"purchase_document/{datetime.date.today()}"
    if request.method == 'POST':
        try:
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage(location=purchase_document_path)
                filename = fs.save(myfile.name, myfile)
                purchase_file_path = purchase_document_path + "/" + filename
                full_data = pd.DataFrame()
                stamp_df = pd.DataFrame()
                for stamp_type, stamp in stamp_types.items():
                    inv_stamp_df = process_purchases(purchase_file_path, stamp)
                    if not inv_stamp_df.empty:
                        data = stamp_verifier(inv_stamp_df, stamp_type)
                        if not data.empty:
                            data['denomination'] = stamp
                            full_data = full_data.append(data)
                        stamp_df = stamp_df.append(inv_stamp_df)


                if full_data.empty:
                    for stamp_type, stamp in stamp_types.items():
                        insert_df = stamp_df.loc[stamp_df['denomination'] == stamp].copy()
                        if not insert_df.empty:
                            puchase_insert(insert_df, stamp_type)
                    return render(request, 'purchase_upload.html', {
                        'purchase_upload_status': 0
                    })
                else:
                    full_data = full_data.reset_index(drop=True)
                    full_data = full_data.T.to_dict().values()
                    return render(request, 'purchase_upload.html', {
                        'purchase_upload_status' : 1, 
                        'conflict_df': full_data
                    })
        except Exception:
            return render(request, 'purchase_upload.html', {'purchase_upload_status': 2})
    return render(request, 'purchase_upload.html', {'purchase_upload_status': 2})

def sale_upload(request):
    sale_document_path = f"sale_document/{datetime.date.today()}"
    if request.method == 'POST':
        try:
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage(location=sale_document_path)
                filename = fs.save(myfile.name, myfile)
                sale_file_path = sale_document_path + "/" + filename
                full_data = pd.DataFrame()
                input_sale = pd.DataFrame()
                for stamp_type, stamp in stamp_types.items():
                    stamp_df = process_sales(sale_file_path, stamp)
                    stamp_df['input_denomination'] = stamp
                    input_sale = input_sale.append(stamp_df)
                    if not stamp_df.empty:
                        data = stamp_verifier(stamp_df, stamp_type)
                        if not data.empty:
                            data['db_denomination'] = stamp
                            full_data = full_data.append(data)

                merged = pd.DataFrame()
                if not full_data.empty:
                    merged = pd.merge(input_sale, full_data, on=['stamp_id'])
                    if merged.shape[0] == input_sale.shape[0]:
                        for stamp_type, stamp in stamp_types.items():
                            update_df = input_sale.loc[input_sale['denomination'] == stamp] .copy()
                            if not update_df.empty:
                                stamp_sold(update_df, stamp_type)
                        return render(request, 'sale_upload.html', {
                            'sale_upload_status': 0
                        })
                    else:
                        missing_df = input_sale.loc[~input_sale.stamp_id.isin(merged.stamp_id.tolist())].copy()
                        missing_df = missing_df.T.to_dict().values()
                        return render(request, 'sale_upload.html', {
                            'sale_upload_status' : 1, 
                            'conflict_df': missing_df
                        })
                else:
                    return render(request, 'sale_upload.html', {'sale_upload_status': 2})

                    
        except Exception:
            return render(request, 'sale_upload.html', {'sale_upload_status': 3})

    return render(request, 'sale_upload.html', {'sale_upload_status' : 3})


def download(request):
    if request.method == 'POST':
        is_sale = 0
        tz = pytz.timezone('Asia/Kolkata')
        download_name = "total_stock_"
        timestamp = str(datetime.datetime.now(tz))[0:-13]
        timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %I:%M:%S %p")
        if "sale" in request.POST:
            is_sale = 1
            download_name = "total_sale_"

        download_filename = download_name + str(timestamp) + ".csv"
        final = pd.DataFrame()
        for table_name in stamp_table_and_denomination:
            db = MySQLdb.connect(user='zoomrx', db='stamp_paper', passwd='', host='localhost')
            cursor = db.cursor()
            if is_sale:
                cursor.execute(f"SELECT stamp_id, purchase_date, sold_date, purchaser_details \
                    FROM {table_name} WHERE is_sale = {is_sale} and delete_flag = 0")
                data = pd.DataFrame(cursor.fetchall(), columns=['stamp_id', 'purchase_date', 'sold_date', 'purhcaser_details'])

            else:
                cursor.execute(f'SELECT stamp_id, purchase_date FROM {table_name} WHERE is_sale = {is_sale} and delete_flag = 0')
                data = pd.DataFrame(cursor.fetchall(), columns=['stamp_id', 'purchase_date'])
            data['denomination'] = stamp_table_and_denomination[table_name]
            final = final.append(data)
        db.close()
        print(final)
        response = HttpResponse('')
        response['Content-Disposition'] = 'attachment; filename={}'.format(download_filename)

        writer = csv.writer(response, dialect=csv.excel)
        if is_sale:
            writer.writerow(['stamp_id', 'purchase_date', 'sold_date', 'purchaser_details', 'denomination'])
        else:
            writer.writerow(['stamp_id', 'purchase_date', 'denomination'])
        for _, row in final.iterrows():
            writer.writerow(row)
        return response
    else:
        return render(request, 'home.html')
