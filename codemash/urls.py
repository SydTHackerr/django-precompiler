from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^contact/', include('contact.urls', namespace='contact')),
    (r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    (r'^accounts/', include('accounts.urls', namespace='account')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'django.contrib.flatpages.views.flatpage', { 'url': '/' },
        name='home'),
)
