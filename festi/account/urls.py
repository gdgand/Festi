from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('account.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)
