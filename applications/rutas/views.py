from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import (TemplateView, ListView, CreateView)

#import models
from .models import rutas
from .forms import NewRutaForm



class PruebaView(TemplateView):
    template_name = 'rutas/prueba.html'


class rutasListView(ListView):
   template_name = "rutas/rutas_list.html"
   model = rutas
   ordering = 'id'
   context_object_name = 'lista_rutas'
   #queryset = ['1', '10']

class rutaCreateView(CreateView):
    template_name = "rutas/crear_ruta.html"
    model = rutas
    fields = ['ruta']
    success_url = reverse_lazy('empleado_app:correcto') 

# class rutasCreateView(FormView):
#     template_name = "rutas/crear_ruta.html"
#     from_class = NewRutaForm
#     fields = ['ruta']
