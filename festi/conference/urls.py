from django.conf.urls import patterns, url

urlpatterns = patterns('conference.views',
    url(r'^$', 'index', name='index'),
)
