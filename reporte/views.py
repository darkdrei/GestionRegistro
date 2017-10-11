# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from supra import views as supra
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
from easy_pdf.views import PDFTemplateView
from django.utils import timezone
from datetime import datetime,timedelta
from usuario import models as usuario
from django.db.models import Q
from django.db import connection
import json as simplejson

# Create your views here.

class Pagos(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        user = CuserMiddleware.get_user()
        emp = empresa.Empresa.objects.filter(supervisor__id=user.id,active=True)
        return render(request, 'reporte/pagos.html',{'empresa':emp})
    # end def
# end class


class Reporte(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'reporte/reportes.html')
    # end def
# end class

def producirFecha(v):
    if v :
        r = v.split('/')
        return '%s-%s-%s'%(r[2],r[1],r[0])
    #end if
    r = datetime.today()
    return '%d-%d-%d'%(r.year,r.month,r.day)
#end def

class WsPagosEmpleados(View):
    def get(self, request):
        print 'llego 1'
        empresa = request.GET.get('empresa', '0')
        ciudad = request.GET.get('ciudad', '0')
        tienda = request.GET.get('tienda', '0')
        inicio = producirFecha(request.GET.get('inicio', '11/09/2017'))
        fecha = datetime.today()
        #fin = producirFecha(request.GET.get('fin', '%d/%d/%d'%(fecha.day,fecha.month,fecha.year)))
        fin = producirFecha(request.GET.get('25/09/2017', '30/09/2017'))
        busqueda = request.GET.get('busqueda', '')
        cursor = connection.cursor()
        m = 'select get_total_trabajador2(%d,\'%s\'::text,%s::integer,%s::integer,%s::integer,\'%s\'::date,\'%s\'::date)' % (
            request.user.id, busqueda, empresa, ciudad, tienda, inicio, fin)
        #cursor.execute('select get_labores();')
        cursor.execute(m)
        row = cursor.fetchone()
        return HttpResponse((simplejson.dumps(row[0])), content_type="application/json")
    # end class
# end class


class WsPagosEmpleados(View):
    def get(self, request):
        print 'llego 2'
        empresa = request.GET.get('empresa', '0')
        ciudad = request.GET.get('ciudad', '0')
        tienda = request.GET.get('tienda', '0')
        fecha = datetime.today() + timedelta(days=1)
        inicio = request.GET.get('inicio','%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        fin = request.GET.get('fin', '%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        busqueda = request.GET.get('busqueda', '')
        print inicio,'  ',fin,request.GET,
        cursor = connection.cursor()
        m = 'SET datestyle = "ISO, DMY";select get_total_trabajador2(%d,\'%s\'::text,%s::integer,%s::integer,%s::integer,\'%s\'::date,\'%s\'::date)' % (
            request.user.id, busqueda, empresa, ciudad, tienda, inicio, fin)
        print m
        cursor.execute(m)
        row = cursor.fetchone()
        return HttpResponse((simplejson.dumps(row[0])), content_type="application/json")
    # end class
# end class

class WsPagosEmpleadosImprimir(PDFTemplateView):
    template_name = "reporte/pagosgeneral.html"

    def get(self, request, *args, **kwargs):
        empleados=','.join( x for x in map(str, request.GET.getlist('reporte','')))
        print empleados
        empresa = request.GET.get('empresa', '0')
        ciudad = request.GET.get('ciudad', '0')
        tienda = request.GET.get('tienda', '0')
        fecha = datetime.today() + timedelta(days=1)
        inicio = request.GET.get('inicio','%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        fin = request.GET.get('fin', '%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        busqueda = request.GET.get('busqueda', '')
        cursor = connection.cursor()
        m = 'SET datestyle = "ISO, DMY";select reporte_general(\'{%s}\'::text,\'%s\'::date,\'%s\'::date);' % (
            empleados, inicio, fin)
        cursor.execute(m)
        row = cursor.fetchone()
        print row[0]
        context = self.get_context_data(**kwargs)
        context.update({'inicio':inicio})
        context.update({'fin':fin})
        context.update({'empleados':row[0]})
        print context
        return self.render_to_response(context)
    # end def
# end


class EmpleadoEspicificoImprimir(PDFTemplateView):
    template_name = "reporte/pagoespeficico.html"

    def get(self, request, *args, **kwargs):
        empleados=','.join( x for x in map(str, request.GET.getlist('reporte','')))
        fecha = datetime.today() + timedelta(days=1)
        inicio = request.GET.get('inicio','%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        fin = request.GET.get('fin', '%d/%d/%d'%(fecha.day,fecha.month,fecha.year))
        busqueda = request.GET.get('busqueda', '')
        cursor = connection.cursor()
        m = 'SET datestyle = "ISO, DMY";select reporte_especifico(\'{%s}\'::text,\'%s\'::date,\'%s\'::date)' % (
            empleados, inicio, fin)
        cursor.execute(m)
        row = cursor.fetchone()
        for x in row[0][0]['data_']:
            print x
        #end for
        context = self.get_context_data(**kwargs)
        context.update({'inicio':inicio})
        context.update({'fin':fin})
        context.update({'empleados':row[0][0]['data_'] if row[0][0]['data_'] else []})
        context.update({'info':row[0][0]['info'][0] if row[0][0]['info'] else []})
        context.update({'total':row[0][0]['ttotal'] if row[0][0]['info'] else []})
        return self.render_to_response(context)
    # end def
# end class
