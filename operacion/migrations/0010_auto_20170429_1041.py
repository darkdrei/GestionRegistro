# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 10:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0009_auto_20170428_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='fin',
            field=models.TimeField(default=datetime.datetime(2017, 4, 29, 10, 41, 31, 401464)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='inicio',
            field=models.TimeField(default=datetime.datetime(2017, 4, 29, 10, 41, 44, 845188)),
            preserve_default=False,
        ),
    ]
