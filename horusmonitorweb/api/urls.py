from django.conf.urls import url, include
from rest_framework import routers
from horusmonitorweb.api import views


urlpatterns = [
    #url(r'^$', include(router.urls)),
    url(r'^machine/(?P<token>[^\s]+)$', views.machine_detail),
    url(r'^os/', views.os_info),
    url(r'^cpu/',views.cpu_info),
    url(r'^memory/', views.memory_info),
    url(r'^disc/', views.disc_info),
    url(r'^service/', views.service_info)
]