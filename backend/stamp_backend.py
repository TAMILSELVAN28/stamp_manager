import pandas as pd
from django.db import models
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from backend.config import stamp_types

from stock_inventory.models import Rs10, Rs20, Rs50, Rs100, Rs500, Rs1000, Rs5000, Rs10000, Rs15000, Rs20000, Rs25000
from django.core.files.storage import FileSystemStorage


def process_purchases(filename, stamp):
    if "csv" in filename:
        purchase_df = pd.read_csv(filename)
    else:
        purchase_df = pd.read_excel(filename)
    stamp_df = purchase_df.loc[purchase_df['denomination'] == stamp].copy()
    stamp_df = stamp_df.dropna(subset=['stamp_id', 'purchase_date'])
    return stamp_df

def process_sales(filename, stamp):
    ignore_list = ['SRO', 'To', 'Total Amount', 'Buyer Name']
    sale_df = pd.read_excel(filename, names=['name', "sold_date", "stamp_type", "denomination", "amount", "stamp_id"])
    sale_df = sale_df.loc[~sale_df['name'].isin(ignore_list)]
    stamp_df = sale_df.loc[sale_df['denomination'] == stamp].copy()
    stamp_df = stamp_df.dropna(subset=['stamp_id'])
    return stamp_df



stamp_object = {
    'Rs10':Rs10, 
    'Rs20':Rs20, 
    'Rs50':Rs50, 
    'Rs100':Rs100, 
    'Rs500':Rs500, 
    'Rs1000':Rs1000,
    'Rs5000':Rs5000,
    'Rs10000':Rs10000,
    'Rs15000':Rs15000,
    'Rs20000':Rs20000,
    'Rs25000':Rs25000
}



def get_obj(obj):
    obj = stamp_object[obj]
    return obj


def stamp_verifier(stamp_records, obj):
    stamp_id_list = tuple(stamp_records['stamp_id'].to_list())
    obj = get_obj(obj)
    data = pd.DataFrame(obj.objects.filter(stamp_id__in=stamp_id_list, delete_flag=0).values('stamp_id'))
    return data


def puchase_insert(stamp_records, obj):
    obj = get_obj(obj)
    for _, row in stamp_records.iterrows():
        obj.objects.create(
            stamp_id=row['stamp_id'],
            purchase_date=row['purchase_date'],
        )

def stamp_sold(stamp_records, obj):
    obj = get_obj(obj)
    for _, row in stamp_records.iterrows():
        stmp_obj = obj.objects.get(
            stamp_id=row['stamp_id']
        )
        stmp_obj.is_sale = 1
        stmp_obj.sold_date = row['sold_date']
        stmp_obj.purchaser_details = row['name']
        stmp_obj.save()


