from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django.contrib.auth import authenticate

from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)



class RegisterCustomUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'form-control text-dark', 'placeholder': 'Введите email'
    }))
    password1 = forms.CharField(label="Введите пароль",widget=forms.PasswordInput(attrs={
        'class': 'form-control text-dark', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control text-dark', 'placeholder': 'Повторите пароль'
    }))



    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')



class LoginCustomUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control text-dark', 'placeholder': 'Email'
    }))
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput(attrs={
        'class': 'form-control text-dark', 'placeholder': 'Password'
    }))
