from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import UserCreationForm


def profile(request):
    return render(request, "accounts/profile.html")


def create_account(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            user = authenticate(username=form.cleaned_data["username"],
                    password=form.cleaned_data["password1"])
            login(request, user)

            return redirect("account:profile")

    return render(request, "accounts/create.html", {
        "form": form,
    })
