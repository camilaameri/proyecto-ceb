from django.shortcuts import render
from .models import Noticia, Comentario
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# from django.views.generic.detail import DetailView


def noticias(request):    
    noticias = Noticia.objects.all()
    paginator = Paginator(noticias, 3)
    pagina = request.GET.get('page') or 1
    noticias = paginator.get_page(pagina)
    currents_page = int(pagina)
    paginas = range(1, noticias.paginator.num_pages + 1)
    return render(request, 'noticias/noticias.html', {'noticias': noticias, 'currents_page': currents_page, 'paginas': paginas})
    # return render(request, 'noticias/noticias.html', {'noticias': noticias})

def ListarPatronales(request):
    noticias = Noticia.objects.all().filter(categoria=1)
    paginator = Paginator(noticias, 3)
    pagina = request.GET.get('page') or 1
    noticias = paginator.get_page(pagina)
    currents_page = int(pagina)
    paginas = range(1, noticias.paginator.num_pages + 1)
    return render(request, 'noticias/noticias.html', {'noticias': noticias, 'currents_page': currents_page, 'paginas': paginas})

def ListarSociales(request):
    noticias = Noticia.objects.all().filter(categoria=2)
    paginator = Paginator(noticias, 3)
    pagina = request.GET.get('page') or 1
    noticias = paginator.get_page(pagina)
    currents_page = int(pagina)
    paginas = range(1, noticias.paginator.num_pages + 1)
    return render(request, 'noticias/noticias.html', {'noticias': noticias, 'currents_page': currents_page, 'paginas': paginas})

def ListarporFecha(request):
    noticias = Noticia.objects.all().order_by('-created')
    paginator = Paginator(noticias, 3)
    pagina = request.GET.get('page') or 1
    noticias = paginator.get_page(pagina)
    currents_page = int(pagina)
    paginas = range(1, noticias.paginator.num_pages + 1)
    return render(request, 'noticias/noticias.html', {'noticias': noticias, 'currents_page': currents_page, 'paginas': paginas})


def detalleNoticias(request, pk):

    notis = Noticia.objects.get(pk=pk)
    return render(request, 'noticias/detalleNoticias.html', {'notis': notis})

def Agregar_Comentario(request, pk):
    texto_comentario = request.POST.get('Coment')
    noti = Noticia.objects.get(pk = pk)
    c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

    return HttpResponseRedirect(reverse_lazy('noticias:detalleNoticias', kwargs={'pk': pk}))





# class Detalle_Noticia_Clase(DetailView):
#     model = Noticia
#     template_name = 'noticias/detalleNoticias.html'