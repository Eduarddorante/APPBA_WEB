from django import forms
from .models import *
from APPBA_WEB.apps.utils.forms_date import DateInput

###################FORMULARIO DANZA#######################
class formularioRegistroForm(forms.ModelForm):

	class Meta:
		model = Registro

		fields = [
			'cedula_alumno',
			'Nombre',
			'Apellido',
			'Fecha_nacimiento',
			'Sexo',
			'Direccion_habitacion',
			'Telefono',
			'Celular',
			'Nivel_instruccion',
			'Email',
			'Institucion_cursante',
			'Curso_realizar',
			'Cursa_otra_actividad',
			'Musica',
			'Danza',
			'Teatro',
			'Artes_Plasticas',

			'cedula_representante',
			'Nombre_Repre',
			'Apellid_Repre',
			'Telefono_repre',
		]

		widgets = {
        'Fecha_nacimiento': DateInput(format='%Y-%m-%d'),
        }
        
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kargs)
			for filed in self.fields:
				self.fields[filed].widgets.attrs.update({'class':'form-control'})

