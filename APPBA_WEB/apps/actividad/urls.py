from django.conf.urls import url
from django.contrib.auth.views import login_required
from ...apps.actividad.views import *

urlpatterns = [

	url(r'^nueva_actividad/$', actiCreateView.as_view(),name="actividadR"),
	url(r'^listado_de_actividades/$', activListView.as_view() ,name="list_actividades"),
	url(r'^editar_actividad/(?P<pk>\d+)$', activUpdateView.as_view(),name='editar_acti'),
	url(r'^eliminar/(?P<pk>\d+)$', activDeleteView.as_view(),name='eliminar_acti'),
    url(r'^calendario/', event),


] 
