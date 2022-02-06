from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        # has to be used instead of models.User when User is modified
        User = get_user_model()
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
