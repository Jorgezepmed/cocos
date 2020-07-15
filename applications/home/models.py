from django.db import models

# Create your models here.
from applications.rutas.models import rutas
from applications.empleados.models import empleados
from applications.camiones.models import camiones

# Create your models here.
class Prueba(models.Model):
    contador = models.CharField('contador', max_length=50)
    chofer = models.ForeignKey(empleados, on_delete=models.CASCADE)
    unidad = models.ForeignKey(camiones, on_delete=models.CASCADE)
    ruta = models.ForeignKey(rutas, on_delete=models.CASCADE)