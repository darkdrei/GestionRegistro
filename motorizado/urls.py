from django.conf.urls import url
import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#Inicio de session
urlpatterns = [
    url(r'^motos/$',login_required(TemplateView.as_view(template_name='motorizado/motos.html')), name='infomoto'),
    url(r'^add/moto/$',login_required(views.AddMoto.as_view()) ,name='add_moto'),
    url(r'^edit/moto/(?P<pk>\d+)/$',login_required(views.AddMoto.as_view()) ,name='edit_moto'),
    url(r'^delete/moto/(?P<pk>\d+)/$',login_required(views.DeleteMoto.as_view()) ,name='delete_moto'),
    url(r'^list/moto/',login_required(views.ListMoto.as_view()) ,name='lis_moto'),
]
