from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView,)

#import models
from .models import camiones



class PruebaView(TemplateView):
    template_name = 'camiones/prueba.html'


class camionesListView(ListView):
   template_name = "camiones/camiones_list.html"
   model = camiones
   ordering = 'id'
   context_object_name = 'lista_camiones'
   #queryset = ['1', '10']



class camionesCreateView(CreateView):
    template_name = "camiones/crear_camion.html"
    model = camiones
    fields = ['unidad']
    success_url = reverse_lazy('empleado_app:correcto') 

class CamionUpdateView(UpdateView):
    template_name = "camiones/update_camiones.html"
    model = camiones
    fields = ['unidad']
    success_url = reverse_lazy('empleado_app:correcto')  

class CamionesDeleteView(DeleteView):
    template_name = "empleados/delete.html"
    model = camiones
    success_url = reverse_lazy('empleado_app:correcto')  