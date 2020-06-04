from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import Profile

from .models import PlayerClaim

from django.contrib.auth.models import User


class PlayerClaimForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя и фамилия (или псевдоним):', widget=forms.TextInput(attrs={'class': 'form-control'}))
    vk = forms.CharField(label='Ссылка на ваш ВК:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Расскажите о себе:', widget=forms.Textarea(attrs={'placeholder': 'Напишите немного о себе (можно о персонаже)', 'class': 'form-control'}))

    class Meta:
        model = PlayerClaim
        fields = ['name', 'vk', 'description']
