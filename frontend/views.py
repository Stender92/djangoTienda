from django.shortcuts import render, redirect
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
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Tijeras')
    datos = {"productos": productoscat}
    return render(request, 'tijeras.html', datos)

def añadir(request):
    v_productos=Producto.objects.all()
    datos={'productos': v_productos}
    return render(request, 'añadir.html', datos)

def guardarProducto(request):
    
    v_idproducto=request.POST.get('idProducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')
    v_categoria=request.POST.get('categoria')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombre=v_nomproducto
    nuevo.stock=v_stockproducto
    nuevo.precio=v_preproducto
    nuevo.categoria=Categoria.objects.get(idCategoria=v_categoria)

    Producto.save(nuevo)

    return redirect('/')

def eliminarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    if(buscado):
        Producto.delete(buscado)
        return redirect('/')

def buscarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscado}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscado=Producto.objects.get(idProducto=v_idproducto)

    if(buscado):
        buscado.nombre=v_nomproducto
        buscado.stock=v_stockproducto
        buscado.precio=v_preproducto

        Producto.save(buscado)
        return redirect('/')





