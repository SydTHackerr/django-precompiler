from django.db import models
from django.contrib.auth.models import User


class TimeSlot(models.Model):

    slot = models.DateTimeField()

    def __str__(self):
        return self.slot.strftime("%A, %B %d, %Y @ %I:%M %p")

    def __unicode__(self):
        return unicode(str(self))


class Location(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(str(self))


class TalkType(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(str(self))


class AudienceSkillLevel(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(str(self))


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(str(self))

    class Meta:
        verbose_name_plural = "Categories"


class TalkManager(models.Manager):

    def all_approved(self):
        return self.get_query_set().filter(approved=True)

    def for_user(self, user):
        return self.get_query_set().filter(proposers=user)


class Talk(models.Model):

    objects = TalkManager()

    title = models.CharField(max_length=255)

    approved = models.NullBooleanField()
    recording_release = models.BooleanField(default=False)

    type = models.ForeignKey(TalkType)
    category = models.ForeignKey(Category)
    audience_skill_level = models.ForeignKey(AudienceSkillLevel)
    location = models.ForeignKey(Location, blank=True, null=True)
    time_slot = models.ForeignKey(TimeSlot, blank=True, null=True)
    proposers = models.ManyToManyField(User)

    outline = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(str(self))
