from django.shortcuts import render
from frontend.models import Categoria

# Create your views here.

def index(request):
    categorias = Categoria.objects.all()
    datos = {'listaCategorias': categorias}
    return render(request, 'index.html', datos)

def nosotros(request):
    return render(request, 'nosotros.html')

def inicio(request):
    return render(request, 'index.html')

def aspersores(request):
    return render(request, 'aspersores.html')

def carrito(request):
    return render(request, 'carrito.html')

def fertilizante(request):
    return render(request, 'fertilizante.html')

def login(request):
    return render(request, 'login.html')

def macetas(request):
    return render(request, 'macetas.html')

def pistolas(request):
    return render(request, 'pistolas.html')

def registro(request):
    return render(request, 'registro.html')

def semillas(request):
    return render(request, 'semillas.html')

def suscripciones(request):
    return render(request, 'suscripciones.html')

def tijeras(request):
    return render(request, 'tijeras.html')




