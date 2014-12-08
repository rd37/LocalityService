'''
Created on Nov 30, 2014

@author: ronaldjosephdesmarais
'''
from django.conf.urls import patterns, include, url

from locality3d import views 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^update/', views.update, name='update'),
    url(r'^search/', views.search, name='search'),
)