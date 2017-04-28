# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 17:24
from __future__ import unicode_literals

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
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'numero no valida')])),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_empresas/')),
                ('web', models.URLField()),
                ('direccion', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Ciudad')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('fijo', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono Fijo')),
                ('celular', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono Celular')),
                ('status', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Ciudad')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa')),
            ],
        ),
    ]
