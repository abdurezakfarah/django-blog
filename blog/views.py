from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreatePost
from .models import Post


def posts(request):
    posts_list = Post.objects.all().order_by("date")
    return render(request, "blog/posts.html", {"posts": posts_list})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/post.html", {"post": post})


@login_required(login_url="/users/login")
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("blog:blog")
        return render(request, "blog/create_post.html", {"form": form})

    form = CreatePost()

    return render(request, "blog/create_post.html", {"form": form})
