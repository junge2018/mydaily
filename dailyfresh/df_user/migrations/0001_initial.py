# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.CharField(max_length=30, null=True, blank=True)),
                ('ureceive', models.CharField(max_length=50)),
                ('uaddress', models.CharField(max_length=100)),
                ('upost', models.CharField(max_length=6, null=True, blank=True)),
                ('uphone', models.CharField(max_length=14)),
                ('isdelete', models.BooleanField(default=False)),
                ('udate_time', models.DateTimeField()),
                ('utest1', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dailyfresh_table',
            },
        ),
    ]
