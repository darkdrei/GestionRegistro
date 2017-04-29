# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from supra import views as supra
from usuario import models as usuario
import models
import forms

# Create your views here.
class InlineInfoMotoView(supra.SupraInlineFormView):
	model = usuario.Empleado
	inline_model = models.InfoMoto
	form_class = forms.InfoMotoForm
#end class
