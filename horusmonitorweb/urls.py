"""horusmonitorweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from horusmonitorweb.core import views
from django.conf.urls import include
from horusmonitorweb.core import urls
from horusmonitorweb.core import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('horusmonitorweb.core.urls', namespace='core')),
    url(r'^dashboard/', include('horusmonitorweb.dashboard.urls', namespace='dashboard')),
    url(r'^accounts/', include('horusmonitorweb.accounts.urls', namespace='accounts')),
    url(r'^api/', include('horusmonitorweb.api.urls', namespace='api'))
    
]
