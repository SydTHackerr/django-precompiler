from django.conf.urls import patterns, include, url


from talks.views import TalkListView, TalkCreationView, TalkUpdateView


urlpatterns = patterns('talks.views',
    url(r'^(?P<pk>[0-9]+)/$', TalkUpdateView.as_view(), name='update'),
    url(r'^create/$', TalkCreationView.as_view(), name='create'),
    url(r'^$', TalkListView.as_view(), name='index'),
)
