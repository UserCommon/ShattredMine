from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Подтвердите Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }

        error_messages = {
            'username': {
                'max_length': "This writer's name is too long.",
            },
        }
'''
    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
'''


class LoginForm(AuthenticationForm):
    class Meta:
        model = User

        fields = ['username', 'password']

        username = forms.CharField(
            label="Логин",
            widget=forms.TextInput(attrs={'class': 'form-control'}),
        )
        password = forms.CharField(
            label="Пароль",
            widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        )


class ProfileForm(forms.ModelForm):
    skin = forms.ImageField(label="Изменить ваш скин")

    class Meta:

        model = Profile

        fields = ['skin']

    def save(self, commit=True):
        profile = self.instance
        profile.skin = self.cleaned_data['skin']

        if self.cleaned_data['skin']:
            profile.skin = self.cleaned_data['skin']
        if commit:
            profile.save()
        return profile
