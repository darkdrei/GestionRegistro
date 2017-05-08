# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets
from cuser.middleware import CuserMiddleware
from usuario import models as usuario
from empresa import models as empresa
import models
from django.utils import timezone
from django.db.models import Q
import datetime, time

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = models.Configuracion
        fields = '__all__'
        exclude = ['estado']
    #end class

    def clean(self):
        data = super(ConfiguracionForm, self).clean()
        print 'Este es el id -->',self.instance.id
        print data.get('inicio'),data.get('fin')
        if data.get('empresa'):
            if data.get('empresa') and data.get('ciudad'):
                print data.get('empresa'),' ',data.get('ciudad')
                if data.get('inicio'):
                    print 'estro inicio con este valor ',data.get('inicio')
                #end if
                if data.get('fin'):
                    print 'estro inicio con este valor ',data.get('fin')
                #end if
                if data.get('dias'):
                    print 'Este son los dias ',data.get('dias')
                    x =  [j.id for j in data.get('dias')]
                    #print x
                    confi = models.Configuracion.objects.filter(dias__id__in=x,empresa=data.get('empresa'))
                    #print confi
                    dias = models.DiaSemana.objects.filter(Q(Q(id__in=x,configuracion__ciudad=data.get('ciudad'),configuracion__empresa=data.get('empresa'),estado=True)) &
                    Q(
                        Q(
                            Q(configuracion__inicio__lte=data.get('inicio')) & Q(configuracion__fin__gte=data.get('inicio'))
                        ) |
                        Q(
                            Q(configuracion__inicio__lte=data.get('fin')) & Q(configuracion__fin__gte=data.get('fin'))
                        ) |
                        Q(
                            Q(configuracion__inicio__gte=data.get('inicio')) & Q(configuracion__inicio__lte=data.get('fin'))
                        ) |
                        Q(
                            Q(configuracion__fin__gte=data.get('inicio')) & Q(configuracion__fin__lte=data.get('fin'))
                        )
                    )).exclude(configuracion__id=self.instance.id if self.instance.id else 0)
                    dias =dias.values_list('configuracion__empresa__first_name','configuracion__ciudad__nombre','configuracion__inicio','configuracion__fin','nombre')
                    if len(dias):
                        m = ''
                        for d in dias:
                            #men ='Este intervalo se cruza en la ciudad %s de la empresa '%(d.configuracion.ciudad.nombre)
                            #self.add_error('dias', men)
                            i1 = '%s:%s:%s'%(concatenarNumero(d[2].hour),concatenarNumero(d[2].minute),concatenarNumero(d[2].second))
                            i2=  '%s:%s:%s'%(concatenarNumero(d[3].hour),concatenarNumero(d[3].minute),concatenarNumero(d[3].second))
                            #print dir(d[2])
                            m = '%s\n%s de %s se encuentra definido el intervalo %s a %s para el dia %s.'%(m,d[0],d[1],i1,i2,d[4])
                        #end for
                        self.add_error('dias',m)
                    #end if
                    print 'Dias de epresa ---> ', dias,' ---> quedaron'
                #end if
            #end i[]
        #end if
    #end class
#end class

def concatenarNumero(n):
    return '%d'%n if len('  %d'%n)==2 else ('0%d'%n)
#end def

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

    def clean(self):
        data = super(ConfiguracionForm, self).clean()
        print 'Este es el id -->',self.instance.id
        print data.get('inicio'),data.get('fin')
        if data.get('empresa'):
            if data.get('empresa') and data.get('ciudad'):
                print data.get('empresa'),' ',data.get('ciudad')
                if data.get('inicio'):
                    print 'estro inicio con este valor ',data.get('inicio')
                #end if
                if data.get('fin'):
                    print 'estro inicio con este valor ',data.get('fin')
                #end if
                if data.get('dias'):
                    print 'Este son los dias ',data.get('dias')
                    x =  [j.id for j in data.get('dias')]
                    #print x
                    confi = models.Configuracion.objects.filter(dias__id__in=x,empresa=data.get('empresa'))
                    #print confi
                    dias = models.DiaSemana.objects.filter(Q(Q(id__in=x,configuracion__ciudad=data.get('ciudad'),configuracion__empresa=data.get('empresa'),estado=True)) &
                    Q(
                        Q(
                            Q(configuracion__inicio__lte=data.get('inicio')) & Q(configuracion__fin__gte=data.get('inicio'))
                        ) |
                        Q(
                            Q(configuracion__inicio__lte=data.get('fin')) & Q(configuracion__fin__gte=data.get('fin'))
                        ) |
                        Q(
                            Q(configuracion__inicio__gte=data.get('inicio')) & Q(configuracion__inicio__lte=data.get('fin'))
                        ) |
                        Q(
                            Q(configuracion__fin__gte=data.get('inicio')) & Q(configuracion__fin__lte=data.get('fin'))
                        )
                    )).exclude(configuracion__id=self.instance.id if self.instance.id else 0)
                    dias =dias.values_list('configuracion__empresa__first_name','configuracion__ciudad__nombre','configuracion__inicio','configuracion__fin','nombre')
                    if len(dias):
                        m = ''
                        for d in dias:
                            #men ='Este intervalo se cruza en la ciudad %s de la empresa '%(d.configuracion.ciudad.nombre)
                            #self.add_error('dias', men)
                            i1 = '%s:%s:%s'%(concatenarNumero(d[2].hour),concatenarNumero(d[2].minute),concatenarNumero(d[2].second))
                            i2=  '%s:%s:%s'%(concatenarNumero(d[3].hour),concatenarNumero(d[3].minute),concatenarNumero(d[3].second))
                            #print dir(d[2])
                            m = '%s\n%s de %s se encuentra definido el intervalo %s a %s para el dia %s.'%(m,d[0],d[1],i1,i2,d[4])
                        #end for
                        self.add_error('dias',m)
                    #end if
                    print 'Dias de epresa ---> ', dias,' ---> quedaron'
                #end if
            #end i[]
        #end if
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
