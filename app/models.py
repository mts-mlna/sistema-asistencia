from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Asistencia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    hora = models.TimeField(auto_now_add=True)
    fecha = models.DateField(auto_now_add=True)
    materia = models.CharField(max_length=100)
    presente = models.BooleanField(default=False)


    def __str__(self):
        estado = 'Presente' if self.presente else 'Ausente'
        return f"{self.nombre} - {estado} - {self.fecha} {self.hora}"


class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    asistencias = models.ManyToManyField('Asistencia', blank=True)

class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=100)  # Profesor, Preceptor, etc.

class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)


    