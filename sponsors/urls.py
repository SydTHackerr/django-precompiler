from django.conf.urls import patterns, include, url

from sponsors.views import UpdateSponsorView, SponsorshipListView


urlpatterns = patterns('sponsors.views',
    url('(?P<pk>[0-9]+)$', UpdateSponsorView.as_view(), name='update'),
    url(r'^$', SponsorshipListView.as_view(), name='home'),
)
