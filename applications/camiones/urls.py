from django.contrib import admin
from django.urls import path
from . import views

app_name = "camiones_app"

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista_camiones/', views.camionesListView.as_view(), name = 'lista_camiones'),
    path('crear_camion/', views.camionesCreateView.as_view(), name = 'add_camion'),
    path('update_camion/<pk>/',views.CamionUpdateView.as_view(), name ='modificar_camion'),
    path('delete_camion/<pk>/',views.CamionesDeleteView.as_view(), name ='eliminar_camion'),
]