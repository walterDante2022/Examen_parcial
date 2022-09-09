from django.shortcuts import render

from gestion_tareas.models import usuarios_app


# Create your views here.
def login(request):
    if request.method == 'POST':
        nombreUsuario=request.POST.get('nombreUsuario')
        passwordUsuario=request.POST.get('passwordUsuario')
        #validacion de informacion
        print(request)
        print(request.POST)
        print(nombreUsuario)
        print(passwordUsuario)
        #fin validacion

    return render(request,'gestion_tareas/login.html')

def dashboard(request):
      return render(request,'gestion_tareas/dashboard.html')