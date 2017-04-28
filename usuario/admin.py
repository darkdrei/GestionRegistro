# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import models
import forms

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    form = forms.DocumentoForm
#end class

class CargoAdmin(admin.ModelAdmin):
    list_display = ['empresa','nombre']
    form = forms.CargoForm
#end class


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['identificacion','first_name','direccion','tienda']
    form = forms.EmpleadoForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EmpleadoEditForm
        # end if
        return super(EmpleadoAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['identificacion','first_name','direccion','tienda']
    form = forms.AdministradorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.AdministradorEditForm
        # end if
        return super(AdministradorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


# Register your models here.
admin.site.register(models.Documento, DocumentoAdmin)
admin.site.register(models.Cargo, CargoAdmin)
admin.site.register(models.Empleado, EmpleadoAdmin)
admin.site.register(models.Administrador, AdministradorAdmin)
