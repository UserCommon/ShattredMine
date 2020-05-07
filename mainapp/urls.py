from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from .forms import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('news/', PostList.as_view(), name='posts_list_url'),
    path('news/post/create/', PostCreate.as_view(), name='post_create_url'),
    path('news/post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('news/post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('news/post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('news/tag/', tags_list, name='tags_list_url'),
    path('news/tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('news/tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('news/tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('news/tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
