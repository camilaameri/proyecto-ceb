from django.urls import path
from . import views


app_name= 'noticias'
urlpatterns = [
    path("noticias/", views.noticias, name="noticias"),
    path("detalleNoticias/<int:pk>", views.detalleNoticias, name="detalleNoticias"),
    path('listarPorFecha/', views.ListarporFecha, name ='listar_noticiasporfecha'),
    path('listarPatronales/', views.ListarPatronales, name ='listar_noticiasPatronales'),
    path('listarSociales/', views.ListarSociales, name ='listar_noticiassociales'),
    path('add_comentario/<int:pk>', views.Agregar_Comentario, name ='agregar_comentario'),
]