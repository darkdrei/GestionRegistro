# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='ciudad',
        ),
        migrations.AddField(
            model_name='supervisor',
            name='ciudad',
            field=models.ManyToManyField(to='empresa.Ciudad'),
        ),
    ]