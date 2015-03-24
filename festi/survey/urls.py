from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'survey.views.index', name='index'),
    url(r'^v1/', include('survey.api_v1', namespace='v1')),
)
