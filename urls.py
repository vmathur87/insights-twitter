from django.conf.urls import patterns, include, url
from django.contrib import admin
from mytrialapp.views import analysis, getquery, myapp

urlpatterns = patterns('',
    url(r'^app/$', getquery),
    url(r'^analysis/$', analysis),
    url(r'^app2/$', myapp),
)
