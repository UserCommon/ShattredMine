from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path("posts/", PostViewList.as_view(), name="posts"),
    path("posts/<str:slug>/", PostDetailView.as_view(), name="post"),
    path("posts/create/", PostCreateView.as_view(), name="create_post"),
    path("posts/<str:slug>/update/", PostUpdateView.as_view(), name="update_post"),
    path("posts/<str:slug>/delete/", PostDeleteView.as_view(), name="delete_post"),
    path("tags/", TagViewList.as_view(), name="tags"),
    path("tags/<str:slug>/", TagRetrieveView.as_view(), name="tag"),
    path("tags/create/", TagCreateView.as_view()),
])

