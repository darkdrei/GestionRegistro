from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

#empleado
urlpatterns = [
    url(r'^login/empleado/$',login_required(views.LoginEmpleado.as_view()) ,name='login_empleado'),
    url(r'^add/empleado/$',login_required(views.AddEmpleado.as_view()) ,name='add_empleado'),
    url(r'^edit/empleado/(?P<pk>\d+)/$',login_required(views.EditEmpleado.as_view()) ,name='edit_empleado'),
    url(r'^delete/empleado/(?P<pk>\d+)/$',login_required(views.DeleteEmpleado.as_view()) ,name='delete_empleado'),
    url(r'^list/empleado/',login_required(views.ListEmpleado.as_view()) ,name='lis_empleado'),
    url(r'^list/empleados/',login_required(views.ListEmpleados.as_view()) ,name='list_empleados'),
    url(r'^change/pass/empleados/',login_required(views.SetPassWordEmpleado.as_view()) ,name='set_pass_empleado'),
]


#direccionamientos del empleado a nivel de vista
urlpatterns += [
    url(r'^view/empleados/$',login_required(views.GeneralCliente.as_view()), name='view_empleados'),
]


#Inicio de session
urlpatterns += [
    url(r'^login/$',views.Login.as_view(), name='login'),
    url(r'^logout/$',views.Logout.as_view(), name='logout'),
]


# manejo de usuario de empleados escritorio
urlpatterns += [
    url(r'^empleados/$',login_required(views.Empleados.as_view()), name='esc_lis_empleados'),
]


# registro de supervisores
urlpatterns += [
    url(r'^supervisores/$',login_required(views.Supervisores.as_view()), name='supervisoress'),
]
