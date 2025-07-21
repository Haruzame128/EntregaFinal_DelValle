from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"