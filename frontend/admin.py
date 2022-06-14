from django.contrib import admin
from frontend.models import Categoria, Producto, Foto
from back.models import Usuario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Foto)
admin.site.register(Usuario)

