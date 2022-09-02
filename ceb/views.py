from django.shortcuts import render

from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 


def Home(request):
	return render(request, 'home.html')

def registro(request):
	data = {
	'form': CustomUserCreationForm()
	}


def Home(request):
    return render(request, 'home.html')


def Registro(request):
	return render(request, 'usuarios/registro.html', data)


def Historia(request):
    return render(request, 'historia.html')

