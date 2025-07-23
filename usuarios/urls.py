from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('registro/', views.UserRegistrationView.as_view() , name='registro'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', views.LogoutUsuario.as_view(), name='logout'),
    path('perfil/', views.PerfilUsuario.as_view(), name='perfil'),
    path('editar_perfil/', views.EditarPerfilUsuario.as_view(), name='editar_perfil'),
    path('instructores/', views.ListaInstructores.as_view(), name='instructores'),
    path('agregar_instructor/', views.AgregarInstructorView.as_view(), name='agregar_instructor'),
    path('instructores/<int:pk>/', views.InstructorDetailView.as_view(), name='detalle_instructor'),
]