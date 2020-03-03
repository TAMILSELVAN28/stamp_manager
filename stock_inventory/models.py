# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Rs10(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_10'


class Rs100(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_100'


class Rs1000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_1000'


class Rs10000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_10000'


class Rs15000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_15000'


class Rs20(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_20'


class Rs20000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_20000'


class Rs25000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_25000'


class Rs50(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_50'


class Rs500(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_500'


class Rs5000(models.Model):
    stamp_id = models.CharField(unique=True, max_length=45)
    is_sale = models.IntegerField(default=0)
    purchase_date = models.CharField(max_length=45)
    sold_date = models.CharField(max_length=45, blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    purchaser_details = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rs_5000'
