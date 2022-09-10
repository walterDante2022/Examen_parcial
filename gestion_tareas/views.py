from django.shortcuts import render
from django.urls import reverse
from gestion_tareas.models import usuarios_app ,Tarea_app
from django.http import HttpResponseRedirect 
from dateutil.parser import parse


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
      tareas_totales=Tarea_app.objects.all()
      return render(request,'gestion_tareas/dashboard.html',{
        'objTarea':tareas_totales,
      })

def nuevaTarea(request):
    if request.method == 'POST':
        fechaCreacion= request.POST.get('fechaCreacion')
        fechaCreacion=parse(fechaCreacion)
        descripcion= request.POST.get('descipcion_tarea')
        responsable= request.POST.get('usuario_Responsable')
        Tarea_app(fechacreacion_tarea=fechaCreacion,descripcion_tarea=descripcion,usuarioResponsable_tarea=responsable).save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

    return render(request,'gestion_tareas/nuevaTarea.html',{
            'tareas_registradas':Tarea_app.objects.all()
    })