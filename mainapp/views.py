from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .utils import *
from datetime import datetime
from .models import *

from accounts.models import Profile
from rest_framework import viewsets
from .forms import *

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission

from .serializers import *


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class PostViewList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-date_pub')
    permission_classes = (AllowAny,)

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)



class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (AllowAny, )
    lookup_field = 'slug'


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwner, )
    lookup_field = 'slug'


class PostCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)


class PostDeleteView(generics.DestroyAPIView):
    permission_classes = (IsOwner, )
    serializers = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'


class TagViewList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)


class TagRetrieveView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = 'slug'


class TagCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = 'slug'
