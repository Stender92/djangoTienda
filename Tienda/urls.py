from django.contrib import admin
from django.urls import path 
from frontend.views import index, nosotros, inicio, aspersores, carrito, fertilizante, login, macetas, pistolas, productos, registro, semillas, suscripciones, tijeras, productos

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
    path('productos/<codCategoria>', productos)
]
