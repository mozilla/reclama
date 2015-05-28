from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',

    # Base
    url(r'^', include('reclama.sprints.urls')),

    # Admin
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Flatpages
    url(r'^', include('django.contrib.flatpages.urls')),
)
