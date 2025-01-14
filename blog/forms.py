from django.forms import ModelForm

from .models import Post


class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "body", "banner"]
