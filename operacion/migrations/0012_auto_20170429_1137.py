# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0011_auto_20170429_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='fin',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='inicio',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
