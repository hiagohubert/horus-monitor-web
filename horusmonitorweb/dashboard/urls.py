from django.conf.urls import url
from django.contrib import admin
from horusmonitorweb.dashboard import views

urlpatterns = [
	url(r'^$', views.dashboard , name='index'),
	url(r'^addserver/', views.addserver , name='addserver'),
	url(r'^server_dashboard/(?P<machineid>\d+)/$', views.server_dashboard , name='server_dashboard'),
	url(r'^server_discs/(?P<machineid>\d+)/$', views.server_discs , name='server_discs'),
	url(r'^server_services/(?P<machineid>\d+)/$', views.server_services , name='server_services'),
	url(r'^cpu_today/(?P<machineid>\d+)/$', views.cpu_today , name='cpu_today'),
	url(r'^memory_today/(?P<machineid>\d+)/$', views.memory_today , name='memory_today'),
	url(r'^alert_config/(?P<machineid>\d+)/$', views.alert_config , name='alert_config'),
	url(r'^alert_config_list/(?P<machineid>\d+)/$', views.alert_config_list , name='alert_config_list'),
	]