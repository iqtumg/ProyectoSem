from django.db import models

dias = (
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miercoles', 'Miercoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
    ('sabado', 'Sabado'),
    ('domingo', 'Domingo')
)

class Horario(models.Model):
    dia = models.CharField(max_length=10, blank=False,choices=dias, verbose_name='Dias')
    horario_inicio = models.TimeField(verbose_name='Horario Inicio')
    horario_fin = models.TimeField(verbose_name='Horario Fin')

# Create your models here.
class Laboral(models.Model):
    turno = models.CharField()
    horarios = models.ManyToManyField(Horario)

class Retraso(models.Model):
    titulo = models.CharField(max_length=256, blank=False, verbose_name='Titulo')
    dia = models.DateTimeField(verbose_name='Dia')
    descripcion = models.CharField(max_length=256, verbose_name='Descripcion')

