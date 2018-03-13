from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^', include('APPBA_WEB.apps.albums.urls', namespace='albums')),
    
    url(r'^', include('APPBA_WEB.apps.authentication.urls', namespace='aunth')),

    url(r'^', include('APPBA_WEB.apps.actividad.urls', namespace='actividad')),
     	
    url(r'^', include('APPBA_WEB.apps.reportes.urls', namespace='Reportes')),

    url(r'^', include('APPBA_WEB.apps.registro.urls', namespace='registro')),

   
]