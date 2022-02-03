from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
