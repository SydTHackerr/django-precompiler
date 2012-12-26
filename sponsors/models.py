from django.db import models
from django.contrib.auth.models import User


class SponsorshipLevelManager(models.Manager):

    def with_approved(self):
        query = super(SponsorshipLevelManager, self).get_query_set()
        return query.filter(sponsors__approved=True).exclude(sponsors=None)


class SponsorshipLevel(models.Model):

    objects = SponsorshipLevelManager()

    level_name = models.CharField(max_length=255)

    def __str__(self):
        return self.level_name

    def approved_sponsors(self):
        return self.sponsors.filter(approved=True)


class SponsorshipManager(models.Manager):

    def for_user(self, user):
        query = super(SponsorshipManager, self).get_query_set()
        return query.filter(sponsor=user)


class Sponsorship(models.Model):

    objects = SponsorshipManager()

    sponsor = models.ForeignKey(User, related_name="sponsorships")
    level = models.ForeignKey(SponsorshipLevel, related_name="sponsors")

    website = models.URLField(blank=True)
    website_copy = models.TextField(blank=True)
    logo = models.FileField(upload_to="sponsor_logos", null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "{self.sponsor} at {self.level}".format(self=self)
