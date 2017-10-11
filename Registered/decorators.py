from django.shortcuts import render, redirect
from usuario import models as usuario


def user_supervisor(view_func):
    def _check(request, *args, **kwargs):
        if request.user.is_authenticated():
            admin = usuario.Administrador.objects.filter(id=request.user.id).first()
            if admin :
                return redirect('operacion:movil_labores')
            #end if
            return view_func(request, *args, **kwargs)
        #end
        return redirect('usuario:login')
    #end def

    return _check
#end def
