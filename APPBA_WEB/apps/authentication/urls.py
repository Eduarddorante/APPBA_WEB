from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from  APPBA_WEB.apps.authentication.views  import HomeTemplateView,LogoutView
from ...apps.authentication import views


urlpatterns = [

	url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^add/$',views.UsersCreateView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^listado_secretarias/$', views.UserListView.as_view(), name='list_user'),

    url(r'^editar_secretaria/(?P<pk>\d+)$', views.UserUpdateView.as_view(), name='update_user'),

    url(r'^delete/(?P<pk>\d+)$', views.UserDeleteView.as_view(), name='delete_users'),

    url(r'^bienvenido/$', HomeTemplateView.as_view(), name='index'),
    #url(r'^accounts/login/$', ErrorView.as_view(), name='error'),

 
] 


