# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
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
from operacion import models as operacion
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView
from empresa import models as empresa
from django.contrib.auth.views import logout
from django.db.models import Q


class GeneralCliente(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        emp = empresa.Empresa.objects.filter(supervisor__id=user.id,active=True)
        return render(request, 'usuario/usuarios.html',{'empresa':emp})
    # end def
# end class


class Empleados(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        emp = empresa.Empresa.objects.filter(supervisor__id=user.id,active=True)
        return render(request, 'usuario/listarempleados.html',{'empresa':emp})
    # end def
# end class


class Logout(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('usuario:login')
    # end def
# end class

# Create your views here.
class LoginEmpleado(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LoginEmpleado, self).dispatch(*args, **kwargs)
    # end def

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', False)
        passw = request.POST.get('pass', False)
        print 'Usuario---> ',username,'  ',passw
        if username and passw:
            print 'Usuario---> 1'
            user = authenticate(username=username, password=passw)
            if user is not None:
                print 'Usuario---> 2'
                return HttpResponse('[{"status":true,"id":%d}]'%(user.id), content_type='application/json', status=200)
            # end if
        # end if
        print 'Usuario---> 3'
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class Login(BaseFormView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Login, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        return render(request,'usuario/login.html',{})
    #end def

    def post(self, request, *args, **kwargs):
        print request.POST
        username = request.POST.get('user', False)
        passw = request.POST.get('pass', False)
        print 'Usuario---> ',username,'  ',passw
        if username and passw:
            print 'Usuario---> 1'
            user = authenticate(username=username, password=passw)
            if user is not None:
                print 'Usuario---> 2'
                login(request, user)
                administrador = models.Administrador.objects.filter(id=user.id)
                if administrador:
                    print 'administrador---> 2'
                    return redirect('operacion:movil_labores')
                #end if
                supervisor = empresa.Supervisor.objects.filter(id=user.id)
                if supervisor:
                    print 'Suervisor---> 3'
                    return redirect('usuario:view_empleados')
                #end if
                if user.is_superuser :
                    print 'Admin---> 3'
                    return redirect('/admin')
                #end if
                return redirect('usuario:login')
            # end if
        # end if
        print 'Usuario---> 3'
        return redirect('usuario:login')
    # end def
# end class


class AddEmpleado(supra.SupraFormView):
    model = models.Empleado
    form_class = forms.EmpleadoForm
    template_name = 'usuario/addempleado.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddEmpleado, self).dispatch(*args, **kwargs)
    # end def
# end class


class ListEmpleado(supra.SupraListView):
    model = models.Empleado
    search_key = 'q'
    list_display = ['id','identificacion','telefono_fijo','telefono_celular','first_name','last_name','direccion','documento','foto','fecha_nacimiento','documento','tienda']
    search_fields = ['id']
    paginate_by = 10

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListEmpleado, self).dispatch(*args, **kwargs)
    # end def
# end class


class ListEmpleados(supra.SupraListView):
    model = models.Empleado
    search_key = 'q'
    list_display = ['id','identificacion','telefono_fijo','telefono_celular','first_name','last_name','direccion','documento','foto','fecha_nacimiento','servicios','tienda_e','empresa_e','ciudad_e']
    search_fields = ['id']
    paginate_by = 100

    class Renderer:
        empresa_e ='tienda__empresa__first_name'
        ciudad_e = 'tienda__ciudad__nombre'
        tienda_e = 'tienda__nombre'
    #end class

    def servicios(self, obj, row):
        edit = "/usuario/edit/empleado/%d/" % (obj.id)
        delete = "/usuario/delete/empleado/%d/" % (obj.id)
        password = "change/pass/empleados/"
        return {'edit': edit, 'delete': delete,'pass':password}
    # end def

    def get_queryset(self):
        user = CuserMiddleware.get_user()
        emp = empresa.Empresa.objects.filter(supervisor__id=user.id).values_list('id', flat=True)
        print emp
        if self.request.GET.get('pagina', False):
            self.paginate_by = self.request.GET.get('pagina', False)
        #end if
        empr = self.request.GET.get('empresa', False)
        ciud = self.request.GET.get('ciudad', False)
        tiend = self.request.GET.get('tienda', False)
        busqueda = self.request.GET.get('search','')
        print 'Empresa ',empr,'  ciudad ',ciud,' tienda',tiend
        empleado = models.Empleado.objects.filter((Q(first_name__contains=busqueda) | Q(last_name__contains=busqueda) | Q(identificacion__contains=busqueda)) & Q(tienda__empresa__id__in=emp,estado=True))
        if empr and ciud and tiend:
            return empleado.filter(tienda__id=int(tiend), tienda__empresa__id=int(empr),tienda__ciudad__id=int(ciud))
        elif empr and ciud:
            print '****************'
            return empleado.filter(tienda__empresa__id=int(empr),tienda__ciudad__id=int(ciud))
        elif empr:
            return empleado.filter(tienda__empresa__id=int(empr))
        #end if
        return empleado

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListEmpleados, self).dispatch(*args, **kwargs)
    # end def
# end class


class EditEmpleado(supra.SupraFormView):
    model = models.Empleado
    form_class = forms.EmpleadoEditForm
    template_name = 'usuario/addempleado.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(EditEmpleado, self).dispatch(*args, **kwargs)
    # end def
# end class


class DeleteEmpleado(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteEmpleado, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        empr=kwargs['pk']
        if empr:
            print 1
            empre = models.Empleado.objects.filter(id=empr).first()
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


class SetPassWordEmpleado(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SetPassWordEmpleado, self).dispatch(request, *args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):# 359291054481645
        passw = request.GET.get('password',False)
        iden = request.GET.get('identificador',False)
        if passwo and iden :
            emp = models.Empleado.objects.filter(id=request.GET.get('identificador','0')).first()
            if emp :
                    emp.set_password(raw_password=password)
                    emp.save()
                    return HttpResponse('{"r":"Ok"}', content_type="application/json", status=200)
            # end if
            return HttpResponse('{"r":"Campos invalidos"}', content_type="application/json", status=400)
        # end if
        return HttpResponse('{"r":"Campos requeridos"}', content_type="application/json", status=400)
    # end def
#end class
