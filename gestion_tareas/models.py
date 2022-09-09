from django.db import models

# Create your models here.

class usuarios_app(models.Model):
    nombre = models.CharField(max_length=128, default='')
    apellido = models.CharField(max_length=128, default='') 
    psw_usuario = models.CharField(max_length=128, default='')
    codigo_usuario = models.CharField(max_length=128, default='')
    