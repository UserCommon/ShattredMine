from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import SubsriptionPageView, CheckoutView, SuccessView, SurviveView, FormView, AllFormView, CurrentFormView

urlpatterns = [
    path('', SubsriptionPageView.as_view(), name='membership_main_url'),
    path('survive/', SurviveView.as_view(), name='survive_url'),
    path('checkout/', CheckoutView.as_view(), name='checkout_url'),
    path('checkout/form/', FormView.as_view(), name='form_url'),
    path('checkout/form/all/', AllFormView.as_view(), name='all_form_url'),
    path('checkout/form/<int:id>/', CurrentFormView.as_view(), name='current_form_url'),
    path('checkout/success/', SuccessView.as_view(), name='success_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
