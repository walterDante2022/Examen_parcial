# Generated by Django 4.1.1 on 2022-09-09 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_tarea', models.CharField(default='', max_length=128)),
                ('fechacreacion_tarea', models.DateField(default=datetime.date.today)),
                ('fechaentrega_tarea', models.DateField(default=datetime.date.today)),
                ('usuarioResponsable_tarea', models.CharField(default='0', max_length=128)),
                ('estado_tarea', models.CharField(default='Progreso', max_length=128)),
            ],
        ),
    ]
