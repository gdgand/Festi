from django.conf.urls import patterns, include, url

urlpatterns = patterns('survey.views',
    url(r'^(?P<event_slug>[\w-]+)/$', 'detail', name='detail'),
    url(r'^(?P<event_id>\d+)/form/$', 'form', name='form'),
)

urlpatterns += patterns('',
    # url(r'^v1/', include('survey.api_v1', namespace='v1')),
)

