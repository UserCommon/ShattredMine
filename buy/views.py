from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .forms import *

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from .models import *
from django.http import HttpResponse, HttpResponseRedirect

import stripe

stripe.api_key = "sk_test_QEVVBWDUXUSIG6sv3OGiPlSe00tqw3T8EN"

User = get_user_model()


class SubsriptionPageView(View):
    template_name = 'account/buy.html'
    template_error = 'account/error.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class CheckoutView(View, LoginRequiredMixin):

    template = 'checkout.html'

    def get(self, request):
        return render(request, self.template, context={})

    def post(self, request):
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST["name"],
            source=request.POST["stripeToken"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            vk=request.POST["vk"]
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=30000,
            currency='rub',
            description='Купил проходку'
        )

        print('Data:' + str(request.POST))
        return reverse(redirect('success_url', context={}))


class RequestView(View, LoginRequiredMixin):

    template = ''

    def get(self, request):
        pass

    def post(self, request):
        pass
# Create your views here.


class SuccessView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class SurviveView(View):

    def get(self, request):
        return render(request, 'survive.html', context={})

    def post(self, request):
        pass


class FormView(View, LoginRequiredMixin):

    def get(self, request):
        form = PlayerClaimForm()
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, 'form.html', context={'form': form})

    def post(self, request):
        bound_form = PlayerClaimForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return HttpResponseRedirect('/main/')
        else:
            return HttpResponseRedirect('/error/')


class AllFormView(View):

    def get(self, request):
        players_claims = PlayerClaim.objects.all()
        if request.user.is_staff:
            return render(request, 'all_forms.html', context={'players_claims': players_claims})
        else:
            return render(request, 'error.html')


class CurrentFormView(View):

    def get(self, request):
        pass
