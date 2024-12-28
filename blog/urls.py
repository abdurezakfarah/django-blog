from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.posts, name="blog"),
    path("create", views.create_post, name="create"),
    path("<slug:slug>", views.post, name="post"),
]
