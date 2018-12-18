from django.shortcuts import render
from django.contrib import auth
from django import forms

# Create your views here.

class LoginForm(auth.forms.AuthenticationForm):
    username = forms.CharField(label=("Username"), max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=("Password"), max_length=30,
    widget=forms.PasswordInput(attrs={'class': 'form-control',
    'placeholder': 'Пароль'}))
