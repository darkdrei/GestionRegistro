# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorizado', '0003_infomoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomoto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]