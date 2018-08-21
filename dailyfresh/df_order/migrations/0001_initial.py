# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_detail_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_fina', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('count', models.IntegerField(null=True)),
                ('trans_states', models.CharField(max_length=100, null=True, blank=True)),
                ('goods', models.ForeignKey(to='df_goods.Goods_info')),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('ocreat_date', models.DateTimeField(auto_now_add=True)),
                ('omodified_date', models.DateTimeField(auto_now=True)),
                ('ois_pay', models.CharField(max_length=3, null=True, blank=True)),
                ('ototal', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('oaddress', models.CharField(max_length=150, null=True, blank=True)),
                ('oback1', models.CharField(max_length=100, null=True, blank=True)),
                ('user', models.ForeignKey(to='df_user.User_info')),
            ],
            options={
                'db_table': 'order_info',
            },
        ),
        migrations.AddField(
            model_name='order_detail_info',
            name='order',
            field=models.ForeignKey(to='df_order.Order_info'),
        ),
    ]
