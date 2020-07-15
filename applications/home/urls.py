from django.contrib import admin
from django.urls import path
from . import views

app_name = "home_app"


urlpatterns = [
    path('lista_prueba/', views.PruebaListView.as_view()),
    path('index/', views.HomePruebaView.as_view(), name = 'index'),
  ]
