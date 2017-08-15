from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

'''urlpatterns = [
    url(r'login/$', views.custom_login, {'template_name': 'usuario/login.html'}, name='user-login'),
    url(r'logout/$', views.custom_logout, {'next_page': '/', }, name='user-logout'),
]'''

#formularios configuracion
urlpatterns = [
    url(r'^configuraciones/$',login_required(TemplateView.as_view(template_name='operacion/configuraciones.html')), name='configuraciones'),
    url(r'add/configuracion/$',login_required(views.AddConfiguracionWS.as_view()) ,name='add_conf'),
    url(r'edit/configuracion/(?P<pk>\d)/$',login_required(views.AddConfiguracion.as_view()) ,name='edit_conf'),
    url(r'list/configuracion/$',login_required(views.ListConfiguracion.as_view()) ,name='list_conf'),
]


#formularios configuracion
urlpatterns += [
    url(r'add/labor/$',login_required(views.AddLabor.as_view()) ,name='add_labor'),
    url(r'edit/labor/',login_required(views.EditLabor.as_view()) ,name='edit_labor'),
    url(r'delete/labor/(?P<pk>\d)/$',login_required(views.DeleteLabor.as_view()) ,name='delete_labor'),
    url(r'list/labor/$',login_required(views.ListLabor.as_view()) ,name='list_labor'),
]

#funcionalidad de adicional labor
urlpatterns += [
    url(r'labores/$',views.Labores.as_view() ,name='labores'),
    url(r'movil/trabajos/$',login_required(views.MobilLabore.as_view()) ,name='movil_labores'),
    url(r'ws/labor/$',login_required(views.AddWsLabor.as_view()) ,name='ws_labor'),
]
