from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from talks.models import Talk
from talks.forms import TalkForm


class TalkListView(ListView):

    queryset = Talk.objects.all_approved()


class TalkCreationView(CreateView):

    model = Talk
    form_class = TalkForm
    success_url = "/accounts/profile"
