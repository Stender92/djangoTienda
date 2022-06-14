
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario
# Create your views here.

def loginBack(request):
    return render(request, 'login_back.html')

def validarUsuario(request):
    #recibimos los datos desde el formulario que fueron 
    #pasados via POST
    v_email=request.POST.get('email')
    v_password=request.POST.get('password')

    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_email, password=v_password)
    #return HttpResponse("LALALA")
        if usu:
            request.session['usuario'] = v_email
            return redirect('indexback/')

    except:
        return redirect('loginBack/')



def indexBack(request):
    if 'usuario' not in request.session:
        return redirect('loginBack/')

    return render(request, 'index_back.html')