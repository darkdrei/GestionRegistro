# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from supra import views as supra
import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cuser.middleware import CuserMiddleware
from django.views.generic import View, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from empresa import models as empresa
from django.utils import timezone
from datetime import datetime
from usuario import models as usuario
from django.db.models import Q

# Create your views here.

class Pagos(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        emp = empresa.Empresa.objects.filter(supervisor__id=user.id,active=True)
        return render(request, 'reporte/pagos.html',{'empresa':emp})
    # end def
# end class


class Reporte(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'reporte/reportes.html')
    # end def
# end class
