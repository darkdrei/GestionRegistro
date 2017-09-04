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


#reporte depagos
urlpatterns += [
    url(r'^ws/pagos/empledos/imprimir/$',login_required(views.WsPagosEmpleadosImprimir.as_view()), name='ws_pagosg'),
]

#reporte depagos
urlpatterns += [
    url(r'^pagos/empledo/especifico/imprimir/$',login_required(views.EmpleadoEspicificoImprimir.as_view()), name='ws_pagose'),
]
