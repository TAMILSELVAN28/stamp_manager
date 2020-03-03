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
            obj = get_obj(table_name)
            denomination = 0
            extra_col = False
            if table_name == 'select':
                return render(request, 'home.html', {'form': form})
            for key in stamp_types:
                if key == table_name:
                    denomination = stamp_types[key]
                    if "sale" in request.POST:
                        data = obj.objects.filter(is_sale=1, delete_flag=0)
                        extra_col = True
                    else:
                        data = obj.objects.filter(is_sale=0, delete_flag=0)
            return render(request, 'home.html', {'datas': data, 'denomination':denomination, 'extra':extra_col})
    else:
        form = Dropdown()
    return render(request, 'home.html', {'form': form})


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
                for stamp_type, stamp in stamp_types.items():
                    stamp_df = process_purchases(purchase_file_path, stamp)
                    if not stamp_df.empty:
                        data = stamp_verifier(stamp_df, stamp_type)
                        if not data.empty:
                            data['denomination'] = stamp
                            full_data = full_data.append(data)

                if full_data.empty:
                    for stamp_type, stamp in stamp_types.items():
                        puchase_insert(stamp_df, stamp_types)
                    return render(request, 'purchase_upload.html', {
                        'purchase_upload_status': 0
                    })
                else:
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
                    if merged.shape == input_sale.shape:
                        for stamp_type, stamp in stamp_types.items():
                            stamp_sold(stamp_df, stamp_types)
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
            cursor.execute(f'SELECT * FROM {table_name} WHERE is_sale = {is_sale} and delete_flag = 0')
            data = pd.DataFrame(cursor.fetchall())
            final = final.append(data)
        db.close()
        response = HttpResponse('')
        response['Content-Disposition'] = 'attachment; filename={}'.format(download_filename)

        writer = csv.writer(response, dialect=csv.excel)
        for _, row in final.iterrows():
            writer.writerow(row)
        return response
    else:
        return render(request, 'home.html')
