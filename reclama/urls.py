from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Base
    url(r'^', include('reclama.sprints.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
