from django import forms

from sponsors.models import Sponsorship


class UserSponsorshipForm(forms.ModelForm):

    class Meta:
        model = Sponsorship
        fields = ("website", "website_copy", "logo")
