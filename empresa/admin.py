# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import models
import forms
import nested_admin
# Register your models here.


class CiudadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    form = forms.CiudadForm
#end class


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nit','first_name','direccion','ciudad']
    form = forms.EmpresaForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EmpresaEditForm
        # end if
        return super(EmpresaAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


class EmpresaInline(nested_admin.NestedStackedInline):
    model = models.Empresa
    form = forms.EmpresaForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EmpresaEditForm
        # end if
        return super(EmpresaInline, self).get_form(request, obj, *args, **kwargs)
    # end def

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ['identificacion','first_name','last_name','direccion','ciudad']
    form = forms.SupervisorForm
    filter_horizontal =['empresas']
    #inlines = [EmpresaInline]

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.SupervisorEditForm
        # end if
        return super(SupervisorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


class TiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion','referencia','empresa','ciudad']
    form = forms.TiendaForm
#end class


admin.site.register(models.Ciudad, CiudadAdmin)
admin.site.register(models.Empresa, EmpresaAdmin)
admin.site.register(models.Tienda, TiendaAdmin)
admin.site.register(models.Supervisor, SupervisorAdmin)
