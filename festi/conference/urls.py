from django.conf.urls import patterns, url

urlpatterns = patterns('conference.views',
    url(r'^$', 'index', name='index'),
    url(r'^speaker/$', 'speaker', name='speaker'),
    url(r'^about/$', 'about', name='about'),
)
