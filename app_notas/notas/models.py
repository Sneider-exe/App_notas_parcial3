from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    
    nombre_completo = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Nota(models.Model):
    """
    Modelo que representa las notas de cada usuario
    """
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
