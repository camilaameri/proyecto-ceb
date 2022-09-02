from django.urls import path
from . import views


app_name= 'eventos'
urlpatterns = [
    path("eventos/", views.eventos, name="eventos"),
    path("detalleeventos/<int:pk>", views.detalleEventos, name="detalleEventos"),
]