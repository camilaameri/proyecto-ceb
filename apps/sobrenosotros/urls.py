from django.urls import path
from . import views

app_name='sobrenosotros'
urlpatterns = [
    path("sobreNosotros/", views.sobreNosotros, name= "sobreNosotros"),
]
