from datetime import datetime
from django.db import models
import datetime
# Create your models here.

class usuarios_app(models.Model):
    nombre = models.CharField(max_length=128, default='')
    apellido = models.CharField(max_length=128, default='') 
    psw_usuario = models.CharField(max_length=128, default='')
    codigo_usuario = models.CharField(max_length=128, default='')

class Tarea_app(models.Model):
    
    descripcion_tarea = models.CharField(max_length=128, default='')  
    fechacreacion_tarea= models.DateField(default=datetime.date.today)
    fechaentrega_tarea= models.DateField(default=datetime.date.today)
    usuarioResponsable_tarea= models.CharField(max_length=128, default='0')
    estado_tarea=models.CharField(max_length=128, default='Progreso') 

    