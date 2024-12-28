from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, default=None)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.jfif", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Post: {self.title}>"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
