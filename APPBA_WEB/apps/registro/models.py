from __future__ import unicode_literals
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.db import models

#####################MODELO REGISTRO################
class Registro(models.Model):

	sex = (('Masculino','Masculino'),('Femenino','Femenino'))

	ID = models.AutoField(primary_key=True, unique=True)
	cedula_alumno = models.CharField(max_length=8,blank=True)
	Nombre = models.CharField(max_length=50)
	Apellido = models.CharField(max_length=70)
	Fecha_nacimiento = models.DateField(apodo('Fecha De Nacimiento'))
	Sexo= models.CharField(max_length=30, choices=sex, default=0)
	Direccion_habitacion= models.CharField(max_length=70)
	Telefono = models.CharField(max_length=11, blank=True)
	Celular= models.CharField(max_length=11, blank=True)
	Nivel_instruccion= models.CharField(max_length=70)
	Email = models.EmailField()
	Institucion_cursante= models.CharField(max_length=70)
	Curso_realizar= models.CharField(max_length=50)
	Cursa_otra_actividad= models.CharField(max_length=50, blank=True)
	Musica = models.BooleanField(default=False)
	Danza = models.BooleanField(default=False)
	Teatro = models.BooleanField(default=False)
	Artes_Plasticas = models.BooleanField(default=False)

	cedula_representante = models.CharField(apodo('Cedula Del Representante'), max_length=8, blank=True, null=True)
	Nombre_Repre = models.CharField(apodo('Nombre'),max_length=50, blank=True, null=True)
	Apellid_Repre = models.CharField(apodo('Apellido'), max_length=50, blank=True, null=True)
	Telefono_repre = models.CharField(apodo('Telefono'), max_length=11, blank=True, null=True)
	def __str__(self):
		return '{} {}'.format(self.Nombre, self.Apellido)

class Representante(models.Model):
	
	cedula_hijo = models.ManyToManyField(Registro)


	def __str__(self):
		return '{} {} {}'.format(self.cedula, self.Nombre_Repre, self.Apellid_Repre)