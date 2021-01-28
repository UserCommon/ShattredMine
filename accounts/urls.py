from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
#    path('auth/token/', obtain_auth_token, name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('profiles/', ProfileViewList.as_view()),
    path('profiles/<int:pk>/', ProfileRetrieveView.as_view()),
    path('profiles/<int:pk>/update/', ProfileUpdateView.as_view()),
    path('users/', UserViewList.as_view()),
    path('users/register/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserRetrieveView.as_view()),
    path('users/activate/<str:uid>/<str:jwt>', UserActivate.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/logout/', UserLogoutView.as_view()),
    path('profile/info/', ProfileInfoView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
