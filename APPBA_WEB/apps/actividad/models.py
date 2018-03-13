from __future__ import unicode_literals
from django.utils.translation import ugettext, ugettext_lazy as apodo
from django.db import models
from django.utils import timezone
from datetime import datetime, date, timedelta
# Create your models here.
class Actividad(models.Model):

	id = models.AutoField(primary_key=True)
	nombr_acti = models.CharField(apodo("Nombre De La Actividad"),max_length=150,)
	descripcio = models.TextField(apodo("Descripcion"),max_length=500)
	fecha_inic = models.DateField(apodo("Fecha De Inicio"), blank=True, null=True)
	fecha_fina = models.DateField(apodo("Fecha De Culminacion"), blank=True, null=True)
	# status1 = models.BooleanField(default=False)
	# status2 = models.BooleanField(default=False)
	# status3 = models.BooleanField(default=False)

	def __str__(self):
		return '{}'.format(self.nombr_acti)

	def fecha():		
		SHORT_DATETIME_FORMAT = 'm/d/Y P'