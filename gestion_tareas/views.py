from django.shortcuts import render
from django.urls import reverse
from gestion_tareas.models import usuarios_app ,Tarea_app , Curso_app
from django.http import HttpResponseRedirect , HttpResponse
from dateutil.parser import parse
#from colorama import init, Fore, Back, Style


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
      tareas_Usuario=[]
    
      tareas_personales=Tarea_app.objects.filter(usuarioResponsable_tarea='u1')  
      for tarea in tareas_personales:
         tareas_Usuario.append(tarea)

      return render(request,'gestion_tareas/dashboard.html',{
        'objTarea':tareas_personales,
      })

def nuevaTarea(request):
    if request.method == 'POST':
        fechaCreacion= request.POST.get('fechaCreacion')
        fechaCreacion=parse(fechaCreacion)
        fechaEntrega= request.POST.get('fechaEntrega')
        fechaEntrega=parse(fechaEntrega)
        
        descripcion= request.POST.get('descripcion_tarea')
        responsable= request.POST.get('usuario_Responsable')
        Tarea_app(fechacreacion_tarea=fechaCreacion,fechaentrega_tarea=fechaEntrega,descripcion_tarea=descripcion,usuarioResponsable_tarea=responsable).save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

    return render(request,'gestion_tareas/nuevaTarea.html',{
            'tareas_registradas':Tarea_app.objects.all(),
            'cursos_registrados':Curso_app.objects.all(),
    })

    
def editarTarea(request, ind):
    tarea_editar=Tarea_app.objects.get(id=ind)
    if request.method == 'POST':
        fechaCreacion= request.POST.get('fechaCreacion')
        fechaCreacion=parse(fechaCreacion)
        fechaEntrega= request.POST.get('fechaEntrega')
        fechaEntrega=parse(fechaEntrega)
        descripcion_tarea= request.POST.get('descripcion_tarea')
        usuario_Responsable= request.POST.get('usuario_Responsable')
        estado_tarea=request.POST.get('estado_tarea')
        tarea_editar.fechacreacion_tarea=fechaCreacion
        tarea_editar.fechaentrega_tarea=fechaEntrega
        
        tarea_editar.descripcion_tarea=descripcion_tarea
        tarea_editar. usuarioResponsable_tarea=usuario_Responsable
        tarea_editar.estado_tarea=estado_tarea
        tarea_editar.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))

    return render(request,'gestion_tareas/editarTarea.html',{
        'tarea_info' :tarea_editar,
        'tareas_registradas':Tarea_app.objects.all(),
        'cursos_registrados':Curso_app.objects.all(),
    })