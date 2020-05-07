from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .utils import *
from datetime import datetime
from .models import *

from accounts.models import Profile

from .forms import *


# Create your views here.
class MainView(View):

    def get(self, request):
        carousel = CarouselPost.objects.all()
        template = "main.html"
        context = {'carousel': carousel}
        return render(request, template, context)


class PostList(View):

    template = 'news/index.html'

    def get(self, request):
        posts = Post.objects.all()
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            return render(request, 'news/index.html', context={'posts': posts, 'profile': profile})

        else:
            return render(request, 'news/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'news/post_detail.html'


class PostCreate(View):

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        if profile.is_media:
            form = PostForm()
            return render(request, 'news/post_create.html', context={'form': form, 'profile': profile})
        else:
            return render(request, 'error.html')

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        bound_form = PostForm(request.POST, request.FILES)

        if profile.is_media:
            if bound_form.is_valid():
                instance = bound_form.save(commit=False)
                instance.author = Profile.objects.get(user=request.user)
                instance.date_pub = datetime.now()
                instance.save()

                return redirect(instance)
            return render(request, 'news/post_create.html', context={'form': bound_form})
        else:
            return render(request, 'error.html')


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'news/post_delete.html'
    redirect_url = "posts_list_url"


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'news/post_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'news/tag_delete.html'
    redirect_url = "tags_list_url"


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'news/post_delete.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'news/tag_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})

#   create tag can everyone


class TagCreate(View):

    def get(self, request):
        form = TagForm()
        profile = Profile.objects.get(user=request.user)
        return render(request, 'news/tag_create.html', context={'profile': profile, 'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, 'news/tag_create.html', context={'form': bound_form})
