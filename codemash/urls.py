from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url


admin.autodiscover()


urlpatterns = patterns('',
    (r'^contact/', include('contact.urls', namespace='contact')),
    (r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    (r'^accounts/', include('accounts.urls', namespace='account')),
    (r'^sponsors/', include('sponsors.urls', namespace='sponsors')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'django.contrib.flatpages.views.flatpage', { 'url': '/' },
        name='home'),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
