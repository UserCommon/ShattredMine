from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.views.generic import View
from django.views.generic import TemplateView

from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .models import *
from django.http import HttpResponse, HttpResponseRedirect


class ErrorView(View):
    template_name = 'account/error.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class SuccessView(View):
    template_name = 'account/success.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class MainView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            form = ProfileForm()
            context = {'profile': profile, 'form': form}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)

    def post(self, request):
        profile = Profile.objects.all()
        bound_form = ProfileForm(request.POST, request.FILES)
#        context = {'profile': profile, 'bound_form': bound_form}
        if bound_form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.skin = request.FILES['skin']
            profile.save()
            Profile.objects.filter().update(skin=profile.skin)
            return HttpResponseRedirect('/accounts/')
        return render(request, self.template_name, context={'profile': profile, 'bound_form': bound_form})


class LoginView(View):
    template_name = 'account/login.html'
    template_error = 'account/Error.html'

    def get(self, request):
        user = Profile()
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_error)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/accounts/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect('/accounts/login/')
            return render(request, self.template_name, {'form': form})


class RegistrationView(View):
    template_name = 'account/registration.html'
    template_error = 'account/Error.html'

    def get(self, request):
        if not request.user.is_authenticated:
            form = RegisterForm()
            return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_error)

    def post(self, request):
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            user = bound_form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/accounts/')
        return render(request, self.template_name, context={'bound_form': bound_form})


class LogoutView(View):
    template_name = 'account/logout.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class FullLogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/accounts/')


class AccountListView(View):
    template_name = 'account/accountlist.html'
    template_error = 'account/error.html'

    def get(self, request):
        user = Profile()
        context = {}
        if request.user.is_staff:
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_error, context)

# Create your views here.
