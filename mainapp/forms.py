from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # self.cleaned_data.get(slug)

        if new_slug == 'create':
            raise ValidationError('Slug may not be Created')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('This tag is created')
        return new_slug


#    def save(self):
#        new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug = self.cleaned_data['slug'])
#        return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['preview', 'title', 'slug', 'body', 'tags']

        widgets = {
            'preview': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be Created')
        return new_slug
