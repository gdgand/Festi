from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/', include('survey.urls', namespace='survey')),
    url(r'', include('conference.urls', namespace='conference')),
)
