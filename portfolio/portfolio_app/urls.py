from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import index

urlpatterns = patterns('',
    url(r'^$','portfolio_app.views.index', name='index'),
)