# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
from cuser.middleware import CuserMiddleware
from usuario import models as usuario
from empresa import models as empresa
import models
from django.utils import timezone


class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = '__all__'
        exclude = ['estado']
    #end class
#end class


class DiaSemanaForm(forms.ModelForm):
    class Meta:
        model = models.DiaSemana
        fields = ['nombre', 'valor']
        exclude = ['estado']
    #end class
#end class


class ConfiguracionFormView(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = '__all__'
        exclude = ['estado']
    #end class

    def __init__(self, *args, **kwargs):
        super(ConfiguracionFormView, self).__init__(*args, **kwargs)
        user = CuserMiddleware.get_user()
        self.fields['empresa'].queryset = empresa.Empresa.objects.filter(supervisor__user_ptr_id=user.id)
    # end def

    def save(self, commit = True):
        conf = super(ConfiguracionFormView, self).save(commit=False)
        user = CuserMiddleware.get_user()
        #conf.empresa= empresa.Empresa.objects.filter(tienda__empleado__user_ptr_id=user.id).first()
        return conf
    #end def
#end class


class CalendarioForm(forms.ModelForm):
    class Meta:
        model = models.Calendario
        fields = ['year']
        exclude = ['estado']
    #end class
#end class


class DiaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiaForm, self).__init__(*args, **kwargs)
        self.fields['dia'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Dia
        fields = ['year','dia']
        exclude = ['estado']
    #end class
#end class


class LaborForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LaborForm, self).__init__(*args, **kwargs)
        self.fields['ini'].widget = widgets.AdminSplitDateTime()
        self.fields['fin'].widget = widgets.AdminSplitDateTime()
        user = CuserMiddleware.get_user()
        if user:
            self.fields['empleado'].queryset = usuario.Empleado.objects.filter(tienda__empresa__supervisor__user_ptr_id=user.id)
        #end if
    # end def

    class Meta:
        model = models.Labor
        fields = ['empleado','ini','fin']
        exclude = ['estado']
    #end class

    def save(self, commit = True):
        conf = super(LaborForm, self).save(commit=False)
        return conf
    #end def
#end class


class LaborFormView(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LaborFormView, self).__init__(*args, **kwargs)
        user = CuserMiddleware.get_user()
        if user:
            self.fields['empleado'].queryset = usuario.Empleado.objects.filter(supervisor__user_ptr_id=user.id)
        #end if
    # end def

    def clean(self):
        data = super(LaborFormView, self).clean()
        emp = data.get('empleado')
        if emp:
            print emp.id,' Ide del estudiante'
            lab = models.Labor.objects.filter(empleado__id=emp.id, estado=True, cerrado=False).first()
            if lab:
                self.add_error('empleado', 'Tiene asiganada una labor.')
            #end if
        #end if

    class Meta:
        model = models.Labor
        fields = ['empleado']
        exclude = ['estado']
    #end class

    def save(self, commit = True):
        labor = super(LaborFormView, self).save(commit=False)
        labor.ini = timezone.now()
        labor.save()
        return labor
    #end def
#end class
