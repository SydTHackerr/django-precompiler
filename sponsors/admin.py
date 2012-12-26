from django.contrib import admin

from sponsors.models import SponsorshipLevel, Sponsorship


admin.site.register(Sponsorship)
admin.site.register(SponsorshipLevel)
