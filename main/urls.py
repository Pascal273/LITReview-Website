from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("following", views.following, name="following"),
    path("ticket/create", views.create_ticket, name="create_ticket"),
    path("review/create/<int:ticket_id>", views.create_review,
         name="create_review"),
    path("no_ticket_review/create", views.create_ticket_with_review,
         name="create_review_with_ticket"),
    path("ticket_review", views.create_review, name="ticket_response")
]
