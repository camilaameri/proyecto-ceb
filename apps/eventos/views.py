from django.shortcuts import render
from .models import Actividades
# Create your views here.
def eventos(request):
    actividades = Actividades.objects.all()
    return render(request, 'eventos/eventos.html', {'actividades': actividades})


def detalleEventos(request, pk):
    activ = Actividades.objects.get(pk=pk)
    return render(request, 'eventos/detalleEventos.html', {'activ': activ})
