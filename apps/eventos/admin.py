from django.contrib import admin
from .models import Instructores, Actividades
# Register your models here.

class InstructoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')
    search_fields = ('nombre',)

class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'lugar')
    search_fields = ('nombre',)


admin.site.register(Instructores, InstructoresAdmin)
admin.site.register(Actividades, ActividadesAdmin)