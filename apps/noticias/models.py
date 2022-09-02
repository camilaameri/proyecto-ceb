from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias')
    autor = models.CharField(max_length=50, null = True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo

    def obtener_comentarios(self):
        return self.mis_comentarios.all()

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, related_name = 'mis_comentarios', on_delete= models.CASCADE)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,related_name='usuario_comentario', on_delete=models.CASCADE)

    def __str__(self):
        return self.texto