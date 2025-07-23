from django.contrib import admin
from django.urls import path, include
from HashiDojo import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acercademi/', views.acercaDeMi, name='acerca_de_mi'),
    path('clases/', views.clases, name='clases'),
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('listaInscriptos/', views.lista_inscriptos, name='lista_inscriptos'),
    path('contacto/', views.contacto, name='contacto'),
    path('inscriptos/<int:pk>/eliminar/', views.InscripcionDeleteView.as_view(), name='eliminar_inscripto'),
    path('sin_permiso/', views.acceso_denegado, name='sin_permiso'),
    path('accounts/', views.acercaDeMi, name='acercademi'),
    path('eventos/', views.ListaEventosView.as_view(), name='lista_eventos'),
    path('eventos/crear/', views.crear_eventos, name='crear_evento'),
    path('eventos/<int:pk>/', views.DetalleEventoView.as_view(), name='detalle_evento'),
    path('eventos/<int:pk>/eliminar/', views.EventoDeleteView.as_view(), name='eliminar_evento'),
]