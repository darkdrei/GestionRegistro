# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Soat(models.Model):
    numeroS = models.CharField(max_length=50, unique=True, validators=[validators.RegexValidator(re.compile('^[0-9]+$'), ('numero no valida'), 'invalid')])
    fecha_expedicionS = models.DateField()
    fecha_expiracionS = models.DateField()

    def __str__(self):
        return self.numeroS

    class Meta:
        verbose_name = "Soat"
        verbose_name_plural = "Soats"
    # end class


class Tecno(models.Model):
    numeroT = models.CharField(max_length=50, unique=True, validators=[
                               validators.RegexValidator(re.compile('^[0-9]+$'), ('numero no valida'), 'invalid')])
    fecha_expedicionT = models.DateField()
    fecha_expiracionT = models.DateField()

    def __str__(self):
        return self.numeroT
    # end def

    class Meta:
        verbose_name = "Tecnomecanica"
        verbose_name_plural = "Tecnomecanicas"
    # end class

TIPO_MOTORIZADO = ((1, 'Planta'), (2, 'Suscrito'))


class Moto(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    placa = models.CharField(max_length=6, unique=True)
    empresaM = models.ForeignKey(Empresa)
    soat = models.OneToOneField(Soat)
    tecno = models.OneToOneField(Tecno)
    t_propiedad = models.CharField(
        ("Tarjeta de Propiedad"), max_length=50, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.placa
    # end def

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"
# end class
