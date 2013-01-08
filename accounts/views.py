from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from talks.models import Talk
from accounts.forms import UserCreationForm


@login_required
def profile(request):
    return render(request, "accounts/profile.html", {
        'proposals': Talk.objects.for_user(request.user),
    })


def create_account(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"])
        login(request, user)

        return redirect("account:profile")

    return render(request, "accounts/create.html", {
        "form": form,
    })
