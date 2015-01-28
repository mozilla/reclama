from django.conf.urls import patterns, url


urlpatterns = patterns(
    'reclama.sprints.views',
    url(r'^$', 'home', name='home'),
    url(r'^e/(?P<slug>[a-z0-9-]+)$', 'event', name='event'),
)
