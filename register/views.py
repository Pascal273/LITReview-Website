from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


def login_page(request):
    failed = False
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            print("Login")
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                failed = True
    return render(request, "authenticate/login.html",
                  {"form": form, "failed": failed})
