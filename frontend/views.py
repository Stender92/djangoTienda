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
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Fertilizantes')
    datos = {"productos": productoscat}
    return render(request, 'fertilizante.html', datos)

def login(request):
    return render(request, 'login.html')

def macetas(request):
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Macetas')
    datos = {"productos": productoscat}
    return render(request, 'macetas.html', datos)

def pistolas(request):
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Pistolas de Riego')
    datos = {"productos": productoscat}
    return render(request, 'pistolas.html', datos)

def registro(request):
    return render(request, 'registro.html')

def semillas(request):
    productoscat = Producto.objects.filter(categoria__nombreCategoria='Semillas')
    datos = {"productos": productoscat}
    return render(request, 'semillas.html', datos)

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
    v_archivoImg=request.POST.get('archivoImg')
    v_descripcion=request.POST.get('descripcion')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')
    v_categoria=request.POST.get('categoria')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombre=v_nomproducto
    nuevo.archivoImg=v_archivoImg
    nuevo.descripcion=v_descripcion
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
    v_archivoImg=request.POST.get('archivoImg')
    v_descripcion=request.POST.get('descripcion')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscado=Producto.objects.get(idProducto=v_idproducto)

    if(buscado):
        buscado.nombre=v_nomproducto
        buscado.archivoImg=v_archivoImg
        buscado.descripcion=v_descripcion
        buscado.stock=v_stockproducto
        buscado.precio=v_preproducto

        Producto.save(buscado)
        return redirect('/')


def indexBack(request):
    return render(request, 'index_back.html')




