from django.db import models


# Create your models here.
class camiones(models.Model):
    unidad = models.CharField('Numero de unidad', max_length=50)


    class Meta:
         verbose_name = "Unidades"    
         verbose_name_plural = "Camiones"
         ordering = ['unidad']
    #     unique_together = ('unidad') #Para que no se repitan dos iguales
   

    def __str__(self):
        return  self.unidad
