from django.db import models


class rutas(models.Model):
    ruta_choices = {
        ('0', 'Ruta 6'),
        ('1', 'Ruta 10'),
        ('2', 'Ruta 8'),
        ('3', 'Ruta 1'),
    }

    ruta = models.CharField('Ruta', max_length=1, choices=ruta_choices)
    
    class Meta:
         verbose_name = "Rutas"    
         verbose_name_plural = "Rutas"
         ordering = ['ruta']
    #     unique_together = ('unidad') #Para que no se repitan dos iguales
    
    def __str__(self):
        return  self.ruta