from django.conf.urls import patterns, include, url


urlpatterns = patterns('contact.views',
    url(r'^thanks/$', 'contact_thanks', name='thanks'),
    url(r'^$', 'contact_form', name='form'),
)
