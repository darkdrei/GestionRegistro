# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import User
from empresa import models as emp
# Create your models here.


class Documento(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    estado= models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s'%self.nombre
    #end def

    def __str__(self):
        return u'%s'%self.nombre
    #end def
#end class


class Usuario(User):
    documento = models.ForeignKey(Documento, verbose_name='Tipo de documento')
    identificacion = models.CharField(max_length=15, unique=True, validators=[
                                      validators.RegexValidator(re.compile('^[0-9]+$'), ('identificacion no valida'), 'invalid')])
    telefono_fijo = models.CharField(verbose_name='Telefono fijo',max_length=15, blank=True, validators=[
                                     validators.RegexValidator(re.compile('^[0-9]+$'), ('telefono no valido'), 'invalid')])
    telefono_celular = models.CharField(verbose_name='Celular',max_length=15, validators=[validators.RegexValidator(
        re.compile('^[0-9]+$'), ('telefono no valido'), 'invalid')])
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def
#end class


class Cargo(models.Model):
    empresa = models.ForeignKey(emp.Empresa)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    estado= models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s'%self.nombre
    #end def

    def __str__(self):
        return u'%s'%self.nombre
    #end def
#end class


class Empleado(Usuario):
    tienda = models.ForeignKey(emp.Tienda)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='empleado/', null=True, blank=True)

    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    #end class
#end class


class Administrador(Usuario):
    tienda = models.ForeignKey(emp.Tienda)
    direccion = models.CharField(max_length=50, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='administrador/', null=True, blank=True)

    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)
    #end def

    class Meta:
        verbose_name = "Administrador Tienda"
        verbose_name_plural = "Administradores de Tiendas"
    #end class
#end class
