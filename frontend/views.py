from django.shortcuts import render
from frontend.models import Categoria, Producto, Foto

# Create your views here.

def index(request):
    #datosCategorias = Categoria.objects.all()
    #datos = {"categorias": datosCategorias}
    fotos = Foto.objects.all()
    datos = {'fotos': fotos} 
    return render(request, 'index.html', datos) #par ordenado de atributo y valor que se van a pasar a la vista

def productos(request, codCategoria):
    v_categoria=Categoria.objects.get(idCategoria=codCategoria)
    v_productos=v_categoria.productos.all()
    datos={"nombreCategoria:":v_categoria.nombreCategoria, "productos":v_productos}
    return render(request, 'verProductos.html', datos)


def nosotros(request):
    return render(request, 'nosotros.html')

def inicio(request):
    return render(request, 'index.html')

def aspersores(request):
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Aspersores')
    datos = {"productos": productoscat}
    return render(request, 'aspersores.html', datos)

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

def indexBack(request):
    return render(request, 'index_back.html')




