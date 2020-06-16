from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import *

from django.contrib.auth.models import User


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            #post = Post.objects.get(slug__iexact=slug)
            obj = get_object_or_404(self.model, slug__iexact=slug)
            return render(request, self.template, context={'profile': profile, self.model.__name__.lower(): obj, 'admin_object': obj})
        else:
            obj = get_object_or_404(self.model, slug__iexact=slug)
            return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        profile = Profile.objects.get(user=request.user)
        if profile.is_media:
            obj = self.model.objects.get(slug__iexact=slug)
            return render(request, self.template, context={self.model.__name__.lower(): obj, 'profile': profile})
        return render(request, 'error.html')

    def post(self, request, slug):
        profile = Profile.objects.get(user=request.user)
        post = self.model.objects.get(slug=slug)
        if profile.is_media and post.author == profile:
            obj = self.model.objects.get(slug__iexact=slug)
            obj.delete()
            return redirect(reverse(self.redirect_url))
        return render(request, 'error.html')


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        profile = Profile.objects.get(user=request.user)

        if profile.is_media:
            obj = self.model.objects.get(slug__iexact=slug)
            bound_form = self.model_form(instance=obj)
            return render(request, self.template,
                          context={'form': bound_form, self.model.__name__.lower(): obj, 'profile': profile})
        return render(request, 'error.html')

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        profile = Profile.objects.get(user=request.user)

        if profile.is_media and bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})
