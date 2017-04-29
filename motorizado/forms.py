# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
from cuser.middleware import CuserMiddleware
from usuario import models as usuario
from empresa import models as empresa
import models
from django.utils import timezone


class InfoMotoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InfoMotoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_expedicionS'].widget = widgets.AdminDateWidget()
        if self.fields['fecha_expedicionS'].widget.attrs.has_key('class'):
            clases =  '%s %s'%(self.fields['fecha_expedicionS'].widget.attrs['class'],'datepicker')
            self.fields['fecha_expedicionS'].widget.attrs.update({'class': clases})
        #end if
        self.fields['fecha_expiracionS'].widget = widgets.AdminDateWidget()
        if self.fields['fecha_expiracionS'].widget.attrs.has_key('class'):
            clases =  '%s %s'%(self.fields['fecha_expiracionS'].widget.attrs['class'],'datepicker')
            self.fields['fecha_expiracionS'].widget.attrs.update({'class': clases})
        #end if
        self.fields['fecha_expedicionT'].widget = widgets.AdminDateWidget()
        if self.fields['fecha_expedicionT'].widget.attrs.has_key('class'):
            clases =  '%s %s'%(self.fields['fecha_expedicionT'].widget.attrs['class'],'datepicker')
            self.fields['fecha_expedicionT'].widget.attrs.update({'class': clases})
        #end if
        self.fields['fecha_expiracionT'].widget = widgets.AdminDateWidget()
        if self.fields['fecha_expiracionT'].widget.attrs.has_key('class'):
            clases =  '%s %s'%(self.fields['fecha_expiracionT'].widget.attrs['class'],'datepicker')
            self.fields['fecha_expiracionT'].widget.attrs.update({'class': clases})
        #end if
        user = CuserMiddleware.get_user()
        self.fields['empleado'].queryset = usuario.Empleado.objects.filter(tienda__empresa__supervisor__user_ptr_id=user.id)
    # end def

    class Meta:
        model = models.InfoMoto
        fields = '__all__'
        exclude = ['estado']
    #end class
#end class
