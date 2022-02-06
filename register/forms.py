from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, label="",
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        label="")
    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
        label="",
    )

    class Meta:
        # get_user_model() instead of models.User when User-model is modified
        User = get_user_model()
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={"placeholder": "Username"}),
        label="",
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        label="",
    )
