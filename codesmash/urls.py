from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/', include('accounts.urls', namespace='account')),
    url(r'^talks/', include('talks.urls', namespace='talks')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.flatpages.views.flatpage',
        {'url': '/' }, name='home'),
)
