from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]