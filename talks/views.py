from django.shortcuts import render
from django.views.generic import ListView

from talks.models import Talk


class TalkListView(ListView):

    queryset = Talk.objects.all_approved()
