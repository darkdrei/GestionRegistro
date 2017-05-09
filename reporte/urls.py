from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#Inicio de session
urlpatterns = [
    url(r'^pagos/$',login_required(views.Pagos.as_view()), name='pagos'),
    url(r'^home/pagos/$',login_required(views.Reporte.as_view()), name='reportes'),
]

#
urlpatterns += [
    url(r'^ws/pagos/empledos/$',login_required(views.WsPagosEmpleados.as_view()), name='ws_pagos'),
]
