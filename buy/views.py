from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.views.generic import View

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .models import *
from django.http import HttpResponse, HttpResponseRedirect


class SubsriptionPageView(View):
    template_name = 'account/buy.html'
    template_error = 'account/error.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)
# Create your views here.
