# Generated by Django 4.1.1 on 2022-09-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_tareas', '0002_tarea_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='usuarios_app',
            name='usuario_curso',
            field=models.CharField(default='', max_length=128),
        ),
    ]
