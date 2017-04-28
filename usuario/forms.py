# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
import models

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = models.Documento
        fields = ['nombre','descripcion']
        exclude = ['status']
    #end class
#end class


class CargoForm(forms.ModelForm):
    class Meta:
        model = models.Cargo
        fields = ['empresa','nombre','descripcion']
        exclude = ['status']
    #end class
#end class


class EmpleadoForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Empleado
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','documento','identificacion',
         'fecha_nacimiento', 'direccion','telefono_fijo', 'telefono_celular', 'tienda']
        exclude = ['estado']
    # end class
#end class


class EmpleadoEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmpleadoEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Empleado
        fields = ['username', 'email', 'first_name','last_name','documento','identificacion',
         'fecha_nacimiento', 'direccion','telefono_fijo', 'telefono_celular', 'tienda']
        exclude = ['estado', 'password1', 'password2']
    # end class
#end class

class AdministradorForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AdministradorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Administrador
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name','documento','identificacion',
         'fecha_nacimiento', 'direccion','telefono_fijo', 'telefono_celular', 'tienda']
        exclude = ['estado']
    # end class
#end class


class AdministradorEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdministradorEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = widgets.AdminDateWidget()
    # end def

    class Meta:
        model = models.Administrador
        fields = ['username', 'email', 'first_name','last_name','documento','identificacion',
         'fecha_nacimiento', 'direccion','telefono_fijo', 'telefono_celular', 'tienda']
        exclude = ['estado', 'password1', 'password2']
    # end class
#end class
