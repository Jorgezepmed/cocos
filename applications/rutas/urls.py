from django.contrib import admin
from django.urls import path
from . import views

app_name = "rutas_app"

urlpatterns = [
    path('lista_rutas/',views.rutasListView.as_view(),name = 'rutas_list'),
    path('prueba_rutas/',views.PruebaView.as_view()),
    path('crear_ruta/', views.rutaCreateView.as_view(), name = 'add_ruta'),



]
