from django.shortcuts import render
from django.urls import reverse
from gestion_tareas.models import usuarios_app 
from django.http import HttpResponseRedirect 


# Create your views here.
def login(request):
    if request.method == 'POST':
        nombreUsuario=request.POST.get('nombreUsuario')
        passwordUsuario=request.POST.get('passwordUsuario')
        
        #validacion de informacion
        usuario_registrado=0
        usuarios_totales=usuarios_app.objects.all()

        for usuario in usuarios_totales:
            if usuario.nombre == nombreUsuario and usuario.psw_usuario == passwordUsuario:
                usuario_registrado=1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request,'gestion_tareas/login.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })


    return render(request,'gestion_tareas/login.html')

def dashboard(request):
      return render(request,'gestion_tareas/dashboard.html')

def nuevaTarea(request):
    return render(request,'gestion_tareas/nuevaTarea.html')