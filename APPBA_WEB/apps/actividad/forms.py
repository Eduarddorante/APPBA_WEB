#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from ...apps.actividad.models import *
from ...apps.utils.forms_date import DateInput
import itertools

###################FORMULARIO ACTIVIDAD###########################
class ActivForm(forms.ModelForm):

	class Meta:
		model = Actividad

		fields = ['nombr_acti', 'descripcio', 'fecha_inic', 'fecha_fina']
		labels = {
		'nombr_acti': 'Nombre De La Actividad',
		'descripcio': 'Descripcion',
		'fecha_inic': 'Fecha De Inicio',
		'hora_inic': 'Hora De Inicio',
		'fecha_fina': 'Fecha De Culminacion',
		'hora_final': 'Hora De Culminacion',
		'status1':'status1',
		'status2':'status2',
		'status3':'status3',
		}
		widgets = {
        'fecha_inic': DateInput(format='%b %d, %Y'),
        'fecha_fina': DateInput(format='%b %d, %Y'),
        }
