# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 22:22
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20170409_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Usuario')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='administrador/')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Tienda')),
            ],
            options={
                'verbose_name': 'Administrador Tienda',
                'verbose_name_plural': 'Administradore de Tienda',
            },
            bases=('usuario.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
