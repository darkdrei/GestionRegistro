# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import decorators
from django.utils.decorators import method_decorator

class Index(TemplateView):

    @method_decorator([login_required, decorators.user_supervisor])
    def dispatch(self, request, *args, **kwargs):
        return render(request, 'Registered/home.html')
    # end def
# end class
