from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path("create/", views.create_post, name="create_post"),
    path("<int:post_id>/edit/", views.edit_post, name="edit_post"),
    path("<int:post_id>/delete/", views.delete_post, name="delete_post"),
    path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
]
