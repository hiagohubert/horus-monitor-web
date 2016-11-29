
from django.conf.urls import include, url
from django.contrib.auth import views
from horusmonitorweb.accounts.views import login_user
from .views import register, edit, edit_password

urlpatterns = [
	 #url(r'^$', dashboard, 
        #name='dashboard'),
	url(r'^entrar/$', login_user, name='login'),
    url(r'^sair/$', views.logout, 
         {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', register, 
          name='register'),
    # url(r'^editar/$', edit, 
    #     name='edit'),
    # url(r'^editar-senha/$', edit_password, 
    #     name='edit_password'),
]
