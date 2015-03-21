from django.conf.urls import patterns, url

urlpatterns = patterns('survey.views',
    url(r'^$', 'index', name='index'),
)
