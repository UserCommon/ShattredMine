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


from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission

from rest_framework.exceptions import PermissionDenied

from .serializers import *
from .permissions import *


class IsProfileOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUserOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return User == request.user


class UserConfirm(APIView):

    def get(self, request):
        pass


class UserViewList(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-date_joined')


class UserRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsUserOwner, ]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class ProfileViewList(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer


class ProfileRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsProfileOwner, ]
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [IsProfileOwner, ]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()


class UserLogoutView(APIView):
    def get(self, request):
        pass


class ProfileInfoView(APIView):
    def get(self, request):
        pass


class UserActivate(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activate/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data = post_data)
        content = result.text()
        return Response(content)