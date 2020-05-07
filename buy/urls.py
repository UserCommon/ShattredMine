from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', SubsriptionPageView.as_view(), name='membership_main_url')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
