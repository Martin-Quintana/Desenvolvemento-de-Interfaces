
from django.db import models


class Cliente(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    fecha_alta = models.DateTimeField("Fecha de alta", blank=False, null=False)
    direccion = models.CharField(max_length=150, blank= False, null=True)
    mobile = models.CharField(max_length=15, blank=False, null=True)



