from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# redirect to Homepage
def index(request):
    return redirect("/home")


@login_required    # redirect to login if not logged in
def home(request):
    return render(request, "main/home.html", {})
