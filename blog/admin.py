from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["title"],
    }
