from django.shortcuts import resolve_url
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

from sponsors.forms import UserSponsorshipForm
from sponsors.models import Sponsorship, SponsorshipLevel


class SponsorshipListView(ListView):

    queryset = SponsorshipLevel.objects.with_approved()


class UpdateSponsorView(UpdateView):

    model = Sponsorship
    form_class = UserSponsorshipForm

    def get_success_url(self):
        return resolve_url("account:profile")

    def get_queryset(self):
        queryset = super(UpdateSponsorView, self).get_queryset()
        return queryset.filter(sponsor=self.request.user)
