from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='accounts_main'),
    path('error/', ErrorView.as_view(), name='error_url'),
    path('success/', SuccessView.as_view(), name='success_url'),
    path('register/', RegistrationView.as_view(), name='register_url'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView.as_view(), name="logout_url"),
    path('logout/sure', FullLogoutView.as_view(), name="fulllogout_url"),
    path('accountslist/', AccountListView.as_view(), name="accountlist_url")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
