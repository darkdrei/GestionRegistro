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
from django.db.models import Q


class ListEmpresa(supra.SupraListView):
    model = models.Empresa
    search_key = 'q'
    list_display = ['id','nit','first_name','direccion','telefono', 'celular', 'ciudad__nombre','tiendas','servicios']
    search_fields = ['id']
    paginate_by = 100

    def servicios(self, obj, row):
        edit = "/empresa/edit/empresa/%d/" % (obj.id)
        delete = "/empresa/delete/empresa/%d/" % (obj.id)
        return {'edit': edit, 'delete': delete}
    # end def

    def tiendas(self, obj, row):
        tienda = models.Tienda.objects.filter(empresa__id=obj.id)
        return len(tienda)
    # end def

    def get_queryset(self):
        queryset = super(ListEmpresa, self).get_queryset()
        user = CuserMiddleware.get_user()
        confi = models.Empresa.objects.filter(supervisor__id=user.id,active=True)
        busqueda = self.request.GET.get('search','')
        confi.filter(Q(ciudad__nombre__contains=busqueda) | Q(first_name__contains=busqueda) | Q(nit__contains=busqueda))
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListEmpresa, self).dispatch(*args, **kwargs)
    # end def
# end class


class Empresas(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        ciu = models.Ciudad.objects.all()
        return render(request, 'empresa/empresa.html',{'ciudad':ciu})
    # end def

# end class


class ListCiudad(supra.SupraListView):
    model = models.Empresa
    search_key = 'q'
    list_display = ['id','nombre','tienda__empresa__id']
    search_fields = ['id']
    paginate_by = 100

    def get_queryset(self):
        queryset = super(ListCiudad, self).get_queryset()
        user = CuserMiddleware.get_user()
        #confi = models.Ciudad.objects.filter(empresa__supervisor__id=user.id,status=True)
        print self.request
        empresa = self.request.GET.get('empresa',False)
        if empresa:
            confi = models.Ciudad.objects.filter(tienda__empresa__supervisor__id=user.id,status=True,tienda__empresa__id=int(empresa)).distinct('id')
        else:
            confi = models.Ciudad.objects.filter(tienda__empresa__supervisor__id=user.id,status=True).distinct('id')
        #end if
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListCiudad, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddEmpresa(supra.SupraFormView):
    model = models.Empresa
    form_class = forms.EmpresaForm
    template_name = 'empresa/addempresa.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddEmpresa, self).dispatch(*args, **kwargs)
    # end def
# end class


class EditEmpresa(supra.SupraFormView):
    model = models.Empresa
    form_class = forms.EmpresaEditForm
    template_name = 'empresa/addempresa.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(EditEmpresa, self).dispatch(*args, **kwargs)
    # end def
# end class


class DeleteEmpresa(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteEmpresa, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        empr=kwargs['pk']
        if empr:
            print 1
            empre = models.Empresa.objects.filter(id=empr).first()
            if empre:
                print 2
                empre.active=False
                empre.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class


class SetPassWordEmpresa(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SetPassWordEmpresa, self).dispatch(request, *args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):# 359291054481645
        password = request.GET.get('password',False)
        identificador = request.GET.get('identificador',False)
        if password and identificador :
            emp = models.Empresa.objects.filter(id=request.GET.get('identificador','0')).first()
            if emp :
                    emp.set_password(raw_password=password)
                    emp.save()
                    return HttpResponse('{"r":"Ok"}', content_type="application/json", status=200)
            # end if
            return HttpResponse('{"r":"Campos invalidos"}', content_type="application/json", status=400)
        # end if
        return HttpResponse('{"r":"Campos requeridos"}', content_type="application/json", status=400)
    # end def
#


class ListTienda(supra.SupraListView):
    model = models.Tienda
    search_key = 'q'
    list_display = ['id','nombre','direccion','ciudad','empresa','fijo']
    search_fields = ['id']
    paginate_by = 10

    def get_queryset(self):
        queryset = super(ListTienda, self).get_queryset()
        user = CuserMiddleware.get_user()
        empresa = self.request.GET.get('empresa',False)
        ciudad = self.request.GET.get('ciudad',False)
        if empresa and ciudad:
            confi = models.Tienda.objects.filter(empresa__supervisor__id=user.id,empresa__id=int(empresa),ciudad__id=int(ciudad),status=True)
        else:
            confi = models.Tienda.objects.filter(empresa__supervisor__id=user.id,status=True)
        #end if
        return confi

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ListTienda, self).dispatch(*args, **kwargs)
    # end def
# end class


class AddTienda(supra.SupraFormView):
    model = models.Tienda
    form_class = forms.TiendaForm
    template_name = 'empresa/addtienda.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddTienda, self).dispatch(*args, **kwargs)
    # end def
# end class


class DeleteTienda(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeleteTienda, self).dispatch(*args, **kwargs)
    # end def

    def get(self, request, *args, **kwargs):
        print request,kwargs
        ti=kwargs['pk']
        if ti:
            print 1
            tien = models.Tienda.objects.filter(id=empr).first()
            if tien:
                print 2
                tien.status=False
                tien.save()
                return HttpResponse('[{"status":true}]', content_type='application/json', status=200)
            # end if
        # end if
        print 3
        return HttpResponse('[{"status":false}]', content_type='application/json', status=202)
    # end def
# end class
