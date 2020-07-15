from django.db import models

# Create your models here.


#Cambiar camioneros a OPERADORES

class empleados(models.Model):
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    cel = models.CharField('Telefono', max_length=10)
    avatar = models.ImageField(upload_to= 'operadores', blank=True, null=True)


    class Meta:
        verbose_name = "Conductor"    
        verbose_name_plural = "Conductores"
        ordering = ['name']
        unique_together = ('name', 'last_name') #Para que no se repitan dos iguales 


    def __str__(self):
        return  self.name + '_' + self.last_name + '_' + str(self.cel) +  '_' + str(self.id)
    