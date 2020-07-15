from django.shortcuts import render

from django.views.generic import (TemplateView, ListView, CreateView)

#import models
from .models import Prueba

# Create your views here.
class PruebaListView(ListView):
   template_name = "home/camiones_lista.html"
   model = Prueba
   context_object_name = 'lista_camiones'
   #queryset = ['1', '10']


class HomePruebaView(TemplateView):
   template_name = "home/index.html"
   