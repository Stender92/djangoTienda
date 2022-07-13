from django.contrib import admin
from django.urls import path, include
from frontend.views import index, nosotros, inicio, aspersores, carrito, fertilizante, login, macetas, pistolas, productos, registro, semillas, suscripciones, tijeras, productos, añadir, guardarProducto, eliminarProducto, buscarProducto, guardarProductoModificado
from back.views import login, validarUsuario, indexBack

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('nosotros.html', nosotros),
    path('index.html', inicio),
    path('aspersores.html', aspersores),
    path('carrito.html', carrito),
    path('fertilizante.html', fertilizante),
    path('login.html', login),
    path('macetas.html', macetas),
    path('pistolas.html', pistolas),
    path('registro.html', registro),
    path('semillas.html', semillas),
    path('suscripciones.html', suscripciones),
    path('tijeras.html', tijeras),
    path('index_back.html', indexBack),
    path('productos/<codCategoria>', productos),
    path('validarUsuario/', validarUsuario),
    path('productos/<codCategoria>', productos),
    path('añadir.html', añadir),
    path('guardarProducto/', guardarProducto),
    path('guardarProductoCambiado/', guardarProductoModificado),
    path('eliminarProducto/<p_idProducto>', eliminarProducto),
    path('modificarProducto/<p_idProducto>', buscarProducto),
    path('api/', include('api.urls')),
    
]
