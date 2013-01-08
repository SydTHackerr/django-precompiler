from django.conf.urls import patterns, include, url


from talks.views import TalkListView, TalkCreationView


urlpatterns = patterns('talks.views',
    url(r'^create/$', TalkCreationView.as_view(), name='create'),
    url(r'^$', TalkListView.as_view(), name='index'),
)
