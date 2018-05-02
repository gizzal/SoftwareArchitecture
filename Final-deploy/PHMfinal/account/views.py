from django.contrib.auth import (
    login as auth_login, logout as auth_logout, authenticate)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.urls import reverse

from account.forms import LoginForm, RegisterForm
from account.models import Profile


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["login"],
                                password=form.cleaned_data["password"])
            if user is not None:
                auth_login(request, user)
                return redirect(reverse("mission_list"))
            else:
                return render(
                    request, "login.html",
                    {"form": form, "errors": ["Incorrect login or password"]})
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


@login_required(login_url="/login")
def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def register(request):
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"])
            p = Profile(user=user)
            p.save()
            return redirect(reverse("login"))
        else:
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html", {"form": RegisterForm()})