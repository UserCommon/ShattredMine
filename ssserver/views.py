from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def redirect_blog(request):
    return HttpResponseRedirect("/main/")
