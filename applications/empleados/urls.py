from django.contrib import admin
from django.urls import path
from . import views

app_name = "empleado_app"

urlpatterns = [
    path('userss/', views.PruebaView.as_view()),
    path('lista_empleados/', views.empleadosListView.as_view(),name = 'users'),
    path('crear_empleado/', views.empleadosCreateView.as_view()),
    path('buscar_empleado/', views.ListaEmpleadosByKword.as_view()),
    path('ver_empleado/<pk>/',views.EmpleadoDetailView.as_view()),
    path('agregar_empleado/',views.EmpleadoCreateView.as_view(), name = 'add'),
    path('success/',views.SuccessView.as_view(), name ="correcto"),
    path('update_empleado/<pk>/',views.EmpleadoUpdateView.as_view(), name ='modificar_empleado'),
    path('delete_empleado/<pk>/',views.EmpleadoDeleteView.as_view(), name ='eliminar_empleado'),
]