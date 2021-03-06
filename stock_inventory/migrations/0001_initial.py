# Generated by Django 3.0.3 on 2020-02-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_10',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs100',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_100',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs1000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_1000',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs10000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_10000',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs15000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_15000',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs20',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_20',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs20000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_20000',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs25000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_25000',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs50',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_50',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs500',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_500',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rs5000',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp_id', models.CharField(max_length=45, unique=True)),
                ('is_sale', models.IntegerField(default=0)),
                ('purchase_date', models.CharField(max_length=45)),
                ('sold_date', models.CharField(blank=True, max_length=45, null=True)),
                ('delete_flag', models.IntegerField(default=0)),
                ('purchaser_details', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'rs_5000',
                'managed': False,
            },
        ),
    ]
