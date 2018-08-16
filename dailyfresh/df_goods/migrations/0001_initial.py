# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to=b'df_goods')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isdelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default=b'500g', max_length=10, null=True)),
                ('gclick_num', models.IntegerField(null=True)),
                ('gdesc', models.CharField(max_length=200, null=True)),
                ('gstorge', models.IntegerField(null=True)),
                ('gcontent', tinymce.models.HTMLField(null=True)),
                ('gcreate_date', models.DateTimeField(auto_now_add=True)),
                ('gmodify_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'dailyfresh_goods',
            },
        ),
        migrations.CreateModel(
            name='Type_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'dailyfresh_type',
            },
        ),
        migrations.AddField(
            model_name='goods_info',
            name='gtype',
            field=models.ForeignKey(to='df_goods.Type_info'),
        ),
    ]
