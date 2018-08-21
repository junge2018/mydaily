from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.order, name='order'),
	url(r'^order_handle/$', views.order_handle, name='order_handle'),
	url(r'^pay_handle/$', views.pay_handle, name='pay_handle'),
	url(r'^pay(\d+)/$', views.pay, name='pay'),

]
