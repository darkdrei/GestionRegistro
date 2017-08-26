# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from supra import views as supra
import forms
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
from motorizado import models as motorizado


# Create your views here.
class AddConfiguracion(supra.SupraFormView):
    model = models.Configuracion
    form_class = forms.ConfiguracionFormView
    template_name = 'operacion/addconfig.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddConfiguracion, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddConfiguracionWS(supra.SupraFormView):
    model = models.Configuracion
    form_class = forms.ConfiguracionFormView
    template_name = 'operacion/addconfig.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddConfiguracionWS, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        return render(request,'operacion/addconfig.html',{'form': forms.ConfiguracionFormView()})
    #end def

    def post(self, request, *args, **kwargs):
        form = forms.ConfiguracionFormView(request.POST, instance=models.Configuracion())
        if form.is_valid():
            confi = form.save(commit=False)
            confi.save()
            return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
        # end if
        error = form.errors.as_json()
        return HttpResponse(error, content_type='application/json', status=404)
    # end def
# end class


class ListConfiguracion(supra.SupraListView):
    model = models.Configuracion
    search_key = 'q'
    list_display = ['id','empresa__first_name','valor','seldias','servicios','inicio','fin','ciudad__nombre']
    search_fields = ['id']
    paginate_by = 100

    def seldias(self, obj, row):
        return 'Lunes martes'
    # end def

    def servicios(self, obj, row):
        edit = "/operarion/edit/configuracion/%d/" % (obj.id)
        delete = "/operarion/delete/configuracion/%d/" % (obj.id)
        add = "/operarion/add/configuracion/"
        return {'edit': edit, 'delete': delete,'add':add}
    # end def

    def get_queryset(self):
        queryset = super(ListConfiguracion, self).get_queryset()
        user = CuserMiddleware.get_user()
        confi = models.Configuracion.objects.filter(empresa__supervisor__user_ptr_id=user.id,estado=True)
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListConfiguracion, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddLabor(supra.SupraFormView):
    model = models.Labor
    form_class = forms.LaborFormView
    template_name = 'operacion/addlabor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddLabor, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddObservacion(supra.SupraFormView):
    model = models.Observacion
    form_class = forms.ObservacionForm
    template_name = 'operacion/addobservacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddObservacion, self).dispatch(*args, **kwargs)
    # end def
# end class


class ListObservacion(supra.SupraListView):
    model = models.Labor
    search_key = 'q'
    list_display = ['id','empleado','ini','nombre','apellidos','identificacion','id_emp','tiempo','servicios','usuario']
    search_fields = ['id','empleado__first_name','empleado__last_name','empleado__identificacion','empleado__username']
    paginate_by = 10

    class Renderer:
        nombre = 'empleado__first_name'
        apellidos = 'empleado__last_name'
        identificacion = 'empleado__identificacion'
        id_emp = 'empleado__id'
        usuario ='empleado__username'
    # end class

    def servicios(self, obj, row):
        edit = "/operacion/edit/labor/"
        return {'edit': edit}
    # end def

    def get_queryset(self):
        queryset = super(ListLabor, self).get_queryset()
        user = CuserMiddleware.get_user()
        tienda = empresa.Tienda.objects.filter(administrador__user_ptr_id=user.id).first()
        busqueda = self.request.GET.get('busq','')
        print self.request.GET
        consulta_tiempo = """select EXTRACT(EPOCH FROM "operacion_labor"."ini")"""
        confi = queryset.filter((Q(empleado__first_name__icontains=busqueda) | Q(empleado__last_name__icontains=busqueda) | Q(empleado__identificacion__icontains=busqueda)) & Q(empleado__tienda__administrador__user_ptr_id=user.id,estado=True,cerrado=False)).extra(select={'tiempo':consulta_tiempo})
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListLabor, self).dispatch(*args, **kwargs)
    # end def
# end class



class ListLabor(supra.SupraListView):
    model = models.Labor
    search_key = 'q'
    list_display = ['id','empleado','ini','nombre','apellidos','identificacion','id_emp','tiempo','servicios','usuario']
    search_fields = ['id','empleado__first_name','empleado__last_name','empleado__identificacion','empleado__username']
    paginate_by = 10

    class Renderer:
        nombre = 'empleado__first_name'
        apellidos = 'empleado__last_name'
        identificacion = 'empleado__identificacion'
        id_emp = 'empleado__id'
        usuario ='empleado__username'
    # end class

    def servicios(self, obj, row):
        edit = "/operacion/edit/labor/"
        return {'edit': edit}
    # end def

    def get_queryset(self):
        queryset = super(ListLabor, self).get_queryset()
        user = CuserMiddleware.get_user()
        tienda = empresa.Tienda.objects.filter(administrador__user_ptr_id=user.id).first()
        busqueda = self.request.GET.get('busq','')
        print self.request.GET
        consulta_tiempo = """select EXTRACT(EPOCH FROM "operacion_labor"."ini")"""
        confi = queryset.filter((Q(empleado__first_name__icontains=busqueda) | Q(empleado__last_name__icontains=busqueda) | Q(empleado__identificacion__icontains=busqueda)) & Q(empleado__tienda__administrador__user_ptr_id=user.id,estado=True,cerrado=False)).extra(select={'tiempo':consulta_tiempo})
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListLabor, self).dispatch(*args, **kwargs)
    # end def
# end class


class EditLabor(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        print '**************************************???'
        return super(EditLabor, self).dispatch(*args, **kwargs)
    # end def

    def post(self, request, *args, **kwargs):
        labor = request.POST.get('id', False)
        if labor:
            print 1
            lab = models.Labor.objects.filter(id=labor).first()
            if lab:
                print 2
                lab.cerrado=True
                lab.fin = timezone.now()
                lab.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class AddWsLabor(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddWsLabor, self).dispatch(*args, **kwargs)
    # end def

    def post(self, request, *args, **kwargs):
        print request.POST,kwargs
        usu = request.POST.get('usuario', False)
        if usu:
            print 1
            lab = models.Labor.objects.filter(empleado__id=int(usu), estado=True, cerrado=False).first()
            if lab:
                return HttpResponse('[{"status":false,"mensaje":"Tiene una labor asignada"}]', content_type='application/json', status=200)
            #end if
            empleado = usuario.Empleado.objects.filter(id=int(usu), estado=True).first()
            if empleado:
                print 'Hora en python ---->',timezone.now(),datetime.today()
                labor = models.Labor(empleado=empleado,ini=timezone.now(), estado=True, cerrado=False)
                labor.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
            return HttpResponse('[{"status":false,"mensaje":"Usuario sin acceso"}]', content_type='application/json', status=200)
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class DeleteLabor(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteLabor, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        labor=kwargs['pk']
        if labor:
            print 1
            lab = models.Labor.objects.filter(id=labor).first()
            if lab:
                print 2
                lab.estado=False
                lab.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class Labores(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'operacion/empleados_tienda.html')
    # end def
# end class


class MobilLabore(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        empleados = motorizado.InfoMoto.objects.filter(empleado__tienda__administrador__user_ptr_id=request.user.id)
        print empleados
        ctx = {'empleados':empleados,'usuario':request.user.username}
        return render(request, 'operacion/listado_labores.html',ctx)
    # end def
# end class
