from django.views.generic import ListView
from django.shortcuts import render, resolve_url
from django.views.generic.edit import CreateView, UpdateView

from talks.models import Talk
from talks.forms import TalkForm


class TalkListView(ListView):

    queryset = Talk.objects.all_approved()


class TalkCreationView(CreateView):

    model = Talk
    form_class = TalkForm

    def get_success_url(self):
        return resolve_url("account:profile")


class TalkUpdateView(UpdateView):

    form_class = TalkForm
    queryset = Talk.objects.all()

    def get_success_url(self):
        return resolve_url("account:profile")

    def get_extra_context_data(self, **kwargs):
        contents = super(TalkUpdateView, self).get_extra_context_data(**kwargs)
        context["editing"] = True
        return context
