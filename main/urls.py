from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("following", views.following, name="following"),
    path("ticket/create", views.create_ticket, name="create_ticket"),
    path("review/create/<int:ticket_id>", views.create_review,
         name="create_review"),
    path("new_review", views.create_ticket_with_review,
         name="create_review_with_ticket"),
    path("ticket_review", views.create_review, name="ticket_response"),
    path("posts", views.posts, name="posts"),
    path("ticket/edit/<int:ticket_id>", views.edit_ticket, name="edit_ticket"),
    path("review/edit/<int:review_id>", views.edit_review, name="edit_review"),
    path("delete/<str:post_type>/<int:post_id>", views.delete_post,
         name="delete_post"),
]
