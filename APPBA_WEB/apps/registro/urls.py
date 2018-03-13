from django.conf.urls import url
from ...apps.registro.views import *


urlpatterns = [

    ##############PAGINA INFORMATIVA##################
    url(r'^Informacion/', informacion ),
    url(r'^Cursos/', cursos.as_view() ),
    url(r'^DANZA/', danza ),
    url(r'^MUSICA/', musica ),
    url(r'^TEATRO/', teatro ),
    url(r'^ARTESPLASTICAS/', artesplasticas),
    url(r'^nacionalista/', nacionalista),
    url(r'^secretaria/', bienvenido),


    ################PAGINAS REGISTRO##################
    url(r'^registrar_alum/', alumnoCreateView.as_view(),name='registro_alumno'),

    ##################PAGINA LISTADO##################
    url(r'^listar_alumno/', registroListView.as_view(), name= 'Lista'),

    ##################MOSTRAR DATOS#####################
    # Esto No Va Asi
    #url(r'^alumno_alumno/$', registroListView.as_view(), name= 'alumno'),
    ####################################################

    #######################EDITAR DATOS##########################
    url(r'^editar/(?P<pk>\d+)$', registroUpdateView.as_view(),name='editar_alumno'),

    ######################ELIMINAR DATOS#########################
    url(r'^borrar/(?P<pk>\d+)$',registroDeleteView.as_view(), name='eliminar_alumno'),
   
    ###################PAGINA INICIO##################
    url(r'^', inicio ),

    ]