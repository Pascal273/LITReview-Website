from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("following", views.following, name="following"),
    path("ticket/create", views.create_ticket, name="create_ticket"),
    path("review/create", views.create_review, name="create_review"),
]
