from atexit import register
from django.contrib import admin
from .models import Categoria, Noticia, Comentario

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'autor', 'categoria')

admin.site.register(Categoria)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentario)