# Generated by Django 3.0.5 on 2021-04-20 11:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last_name')),
                ('wallet_address', models.CharField(max_length=400)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_product_manager', models.BooleanField(default=False)),
                ('is_sales_manager', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('brand', models.CharField(default='Other', max_length=100)),
                ('category', models.CharField(default='Other', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('image', models.CharField(default='#', max_length=1000)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('specs', models.CharField(blank=True, default='', max_length=1000)),
                ('campaign', models.CharField(blank=True, default='', max_length=200)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_counts', models.CharField(max_length=600, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message=None)])),
                ('total_price', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, verbose_name='order_date')),
                ('status', models.IntegerField(choices=[(0, 'Waiting For Payment'), (1, 'Payment Confirmed'), (2, 'Approved'), (3, 'Preparing'), (4, 'Shipped'), (5, 'Delivered'), (6, 'Rejected')], default=0)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(to='core.Item')),
            ],
        ),
    ]
