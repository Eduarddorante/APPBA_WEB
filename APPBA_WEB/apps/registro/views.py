from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from ...apps.registro.models import *
from ...apps.registro.forms import *
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.shortcuts import render
import os
from django.conf import settings
from io import BytesIO
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ...apps.actividad.models import Actividad
from ...apps.utils.mixins import AdminRequiredMixin,UsuarioRequiredMixin


##########################PAGINA INFORMATIVA###########################
def inicio(request):
	return render(request ,"infor/inicio.html")

def informacion(request):
	return render(request, "infor/contact.html")


def danza(request):
	return render(request, "infor/danza.html")

def musica(request):
	return render(request, "infor/musica.html")

def teatro(request):
	return render(request, "infor/teatro.html")

def artesplasticas(request):
	return render(request, "infor/artesplasticas.html")

def nacionalista(request):
	return render(request, "infor/nacionalista.html")

def Ayuda(request):
	return render(request, "secretaria/ayuda.html")

def bienvenido(request):
	
	return render (request, 'secretaria/secretaria.html')



#############ACTIVIDADES##############################

class cursos(ListView):
    context_object_name = 'listar_actividad'
    model = Actividad
    template_name = 'infor/actividad.html'

###########################REGISTROS#####################e

###########################REGISTROS#####################

########################REGISTRO###################
class alumnoCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
	model = Registro
	fields = ['cedula_alumno','Nombre','Apellido','Fecha_nacimiento','Sexo','Direccion_habitacion','Telefono','Celular','Nivel_instruccion','Email','Institucion_cursante','Curso_realizar','Cursa_otra_actividad','Musica','Danza','Teatro','Artes_Plasticas','cedula_representante','Nombre_Repre','Apellid_Repre','Telefono_repre']
	template_name = 'registro/registrar.html'
	success_url = '/listar_alumno/'

######################PAGINAS LISTADOS###################

########################LISTAR#####################
class registroListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
	context_object_name = 'listar_alumno'
	model = Registro
	template_name = 'registro/listar.html'

########################EDITAR###########################
class registroUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
	template_name = 'registro/editar.html'
	model = Registro
	fields = ['ID','Nombre','Apellido','Fecha_nacimiento','Sexo','Direccion_habitacion','Telefono','Celular','Nivel_instruccion','Email','Institucion_cursante','Curso_realizar','Cursa_otra_actividad',
		]
	success_url = '/listar_alumno/'

######################ELIMINAR###########################
class registroDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
	model = Registro
	template_name = 'registro/alum_confirm_delete.html'
	success_url = reverse_lazy('registro:Lista')