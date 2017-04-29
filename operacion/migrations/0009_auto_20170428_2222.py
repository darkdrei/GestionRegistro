# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0008_labor_cerrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Dia de la semana',
                'verbose_name_plural': 'Dias de la semana',
            },
        ),
        migrations.AlterModelOptions(
            name='configuracion',
            options={'verbose_name': 'Configuracion pago por tienda', 'verbose_name_plural': 'Configuraciones pago por tienda'},
        ),
        migrations.RenameField(
            model_name='configuracion',
            old_name='fincho',
            new_name='valor',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='ordinario',
        ),
        migrations.AddField(
            model_name='configuracion',
            name='dias',
            field=models.ManyToManyField(to='operacion.DiaSemana'),
        ),
    ]
