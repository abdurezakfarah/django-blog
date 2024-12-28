from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:blog")
        return render(request, "users/register.html", {"form": form})

    form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


def signin(request):
    full_path = request.get_full_path()
    next = request.GET.get("next", "/")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next)
        return render(
            request, "users/login.html", {"form": form, "full_path": full_path}
        )

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "full_path": full_path})


def sign_out(request):
    logout(request)
    return redirect("users:login")
