from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def login(request):
    return render(request=request, template_name='login.html')

def validarUsuario(request):
    #recibimos los datos desde el formulario que fueron 
    #pasados via POST
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_email, password=v_password)

        if usu:
            request.session['usuario'] = v_email
            return redirect('/index_back.html')

    except:
        return redirect('/login.html')


def indexBack(request):
    if 'usuario' not in request.session:
        return redirect('/login.html')

    return render(request, 'index_back.html')