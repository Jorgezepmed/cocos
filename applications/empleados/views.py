from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView,
    DeleteView,
    )

#import models
from .models import empleados

#import forms
from .forms import empleadoForm



class PruebaView(TemplateView):
    template_name = 'empleados/userss.html'


class empleadosListView(ListView):
   template_name = "empleados/users.html"
   paginate_by = 100
   ordering = 'id'
   context_object_name = 'lista_empleados'
   model = empleados
   #queryset = ['1', '10']

class ListaEmpleadosByKword(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'


    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = empleados.objects.filter(
            name = palabra_clave
        )
        print (lista) 
        return lista

class empleadosCreateView(CreateView):
    template_name = "empleados/crear_empleado.html"
    model = empleados
   
     

class EmpleadoDetailView(DetailView):
    model = empleados
    template_name = "empleados/detail_empleado.html"


    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = "empleados/success.html"

class EmpleadoCreateView(CreateView):
    template_name = "empleados/crear_empleado.html"
    model = empleados
   
    #fields = ['name', 'last_name', 'cel']
    fields = ('__all__')
    success_url = reverse_lazy('empleado_app:correcto')         #Cuando es un punto '.' Es que se recarge a misa pagina


class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = empleados
    fields = ['name', 'last_name', 'cel']
    success_url = reverse_lazy('empleado_app:correcto')   

    

class EmpleadoDeleteView(DeleteView):
    template_name = "empleados/delete.html"
    model = empleados
    success_url = reverse_lazy('empleado_app:correcto')   
    


    
