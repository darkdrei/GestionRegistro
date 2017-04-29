# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 22:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_administrador'),
        ('motorizado', '0002_remove_motorizado_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoMoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licencia', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'licencia no valida', 'invalid')])),
                ('identifier', models.CharField(blank=True, max_length=20, null=True)),
                ('numeroS', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'numero no valida', 'invalid')])),
                ('fecha_expedicionS', models.DateField()),
                ('fecha_expiracionS', models.DateField()),
                ('numeroT', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'numero no valida', 'invalid')])),
                ('fecha_expedicionT', models.DateField()),
                ('fecha_expiracionT', models.DateField()),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=6, unique=True)),
                ('t_propiedad', models.CharField(max_length=50, unique=True, verbose_name='Tarjeta de Propiedad')),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuario.Empleado')),
                ('soat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motorizado.Soat')),
                ('tecno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='motorizado.Tecno')),
            ],
            options={
                'verbose_name': 'Moto Informacion',
                'verbose_name_plural': 'Informaciones de Motos',
            },
        ),
    ]
