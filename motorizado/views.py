# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from supra import views as supra
from usuario import models as usuario
import models
import forms


class AddMoto(supra.SupraFormView):
    model = models.InfoMoto
    form_class = forms.InfoMotoForm
    template_name = 'motorizado/addmoto.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddEmpleado, self).dispatch(*args, **kwargs)
    # end def
# end class


class ListMoto(supra.SupraListView):
    model = models.InfoMoto
    search_key = 'q'
    list_display = ['id','identificacion','placa','marca','numeroS','servicios','tienda_e','empresa_e','ciudad_e','nombre','apellidos']
    search_fields = ['id']
    paginate_by = 100

    class Renderer:
        empresa_e ='empleado__tienda__empresa__first_name'
        ciudad_e = 'empleado__tienda__ciudad__nombre'
        tienda_e = 'empleado__tienda__nombre'
		identificacion = 'empleado__identificacion'
		nombre = 'empleado__firs_name'
		apellidos = 'empleado__last_name'
    #end class

    def servicios(self, obj, row):
        edit = "/morotizado/edit/moto/%d/" % (obj.id)
        delete = "/motorizado/delete/moto/%d/" % (obj.id)
        add = "/motorizado/add/moto/"
        password = "change/pass/empleados/"
        return {'edit': edit, 'delete': delete,'pass':password}
    # end def

    def get_queryset(self):
        user = CuserMiddleware.get_user()
        #emp = models.InfoMoto.objects.filter(empleado__tienda__empresa__supervisor__id=user.id).values_list('id', flat=True)
        print emp
        if self.request.GET.get('pagina', False):
            self.paginate_by = self.request.GET.get('pagina', False)
        #end if
        busqueda = self.request.GET.get('search','')
        print 'Empresa ',empr,'  ciudad ',ciud,' tienda',tiend
        moto = models.InfoMoto.objects.filter((Q(empleado__tienda__empresa__first_name__contains=busqueda) |
		Q(empleado__tienda__ciudad__nombre__contains=busqueda) | Q(empleado__tienda__nombre__contains=busqueda)
		| Q(empleado__firs_name__contains=busqueda) | Q(empleado__last_name__contains=busqueda)
		| Q(placa__contains=busqueda) | Q(marca__contains=busqueda)
		| Q(numeroS__contains=busqueda))
		& Q(empleado__tienda__empresa__supervisor__id=user.id,estado=True))
        return moto

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListMoto, self).dispatch(*args, **kwargs)
    # end def
# end class


class DeleteMoto(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteMoto, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        empr=kwargs['pk']
        if empr:
            print 1
            empre = models.InfoMoto.objects.filter(id=empr).first()
            if empre:
                print 2
                empre.estado=False
                empre.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class
