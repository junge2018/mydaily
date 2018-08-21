# coding=utf-8
from django.conf.urls import url
import views
from views import *
# 从views中将所有的类倒入

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name='list'),
	url(r'^(\d+)/$', views.detail, name='detail'),
	url(r'^search/', MySearchView()),

]