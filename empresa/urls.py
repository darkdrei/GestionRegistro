from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


#Manejo de empresa
urlpatterns = [
    url(r'list/empresa/$', login_required(views.ListEmpresa.as_view()), name='list_empresa'),
    url(r'add/empresa/$', login_required(views.AddEmpresa.as_view()), name='add_empresa'),
    url(r'edit/empresa/(?P<pk>\d+)/$', login_required(views.EditEmpresa.as_view()), name='edit_empresa'),
    url(r'change/pass/empresa/$', login_required(views.SetPassWordEmpresa.as_view()), name='change_pass_empresa'),
    url(r'delete/empresa/(?P<pk>\d+)/$', login_required(views.DeleteEmpresa.as_view()), name='delete_pass_empresa'),
]

#Manejo de tienda
urlpatterns += [
    url(r'list/tienda/$', login_required(views.ListTienda.as_view()), name='list_tienda'),
    url(r'add/tienda/(?P<pk>\d+)/$', login_required(views.AddTienda.as_view()), name='add_tienda'),
    url(r'edit/tienda/(?P<pk>\d+)/$', login_required(views.AddTienda.as_view()), name='edit_tienda'),
    url(r'delete/tienda/(?P<pk>\d+)/$', login_required(views.DeleteTienda.as_view()), name='delete_pass_tienda'),
]

#Manejo de ciudad
urlpatterns += [
    url(r'list/ciudad/$', login_required(views.ListCiudad.as_view()), name='list_ciudad'),
]

#vista
urlpatterns += [
    url(r'ListarEmpresas/$',login_required(views.Empresas.as_view()), name='esc_lis_empresas'),
]
