from django.contrib import admin
from django.urls import path, include
from HashiDojo import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercademi/', views.acercaDeMi, name='acerca_de_mi'),
    path('clases/', views.clases, name='clases'),
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('contacto/', views.contacto, name='contacto'),
]