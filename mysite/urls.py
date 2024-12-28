from django.conf import settings

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path("", include("blog.urls")),
    path("users/", include("users.urls")),
]
