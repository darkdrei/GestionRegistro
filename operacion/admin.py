# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import forms
from django.contrib import admin
import models


class LaborAdmin(admin.ModelAdmin):
    list_display = ['empleado','fin']
    form = forms.LaborForm
#end class


class DiaAdmin(admin.ModelAdmin):
    list_display = ['year','dia']
    form = forms.DiaForm
#end class


class CalendarioAdmin(admin.ModelAdmin):
    list_display = ['year']
    form = forms.CalendarioForm
#end class


class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ['empresa','valor']
    form = forms.ConfiguracionForm
    filter_horizontal = ['dias']
#end class

class DiaSemanaFormAdmin(admin.ModelAdmin):
    list_display = ['nombre','valor']
    form = forms.DiaSemanaForm
#end class


class PagoLaborAdmin(admin.ModelAdmin):
    list_display = ['labor','ini','fin','precio','hora']
#end class

# Register your models here.
admin.site.register(models.Configuracion, ConfiguracionAdmin)
admin.site.register(models.Calendario, CalendarioAdmin)
admin.site.register(models.Dia, DiaAdmin)
admin.site.register(models.Labor, LaborAdmin)
admin.site.register(models.DiaSemana, DiaSemanaFormAdmin)
admin.site.register(models.PagoLabor, PagoLaborAdmin)
