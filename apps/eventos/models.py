
from django.db import models

# Create your models here.

class Instructores(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    def __str__(self):
        return self.nombre
    
class Actividades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='actividades')
    instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
    
    def __str__(self):
        return self.nombre

