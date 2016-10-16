from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Incidente(models.Model):

    time = models.DateTimeField(auto_now_add=True, verbose_name='Tiempo', null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=100)
    descripcion = models.CharField(verbose_name='Descripción', max_length=255)
    ESTADO = (
        ('NUEVO', 'NUEVO'),
        ('EN_CURSO', 'EN CURSO (ASIGNADO)'),
        ('RESULTO', 'RESUELTO'),
        ('FINALIZADO', 'FINALIZADO'),
    )
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO)
    lat = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Latitud')
    log = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Longitud')
    is_active = models.BooleanField(verbose_name='Activo', default=True)
    user = models.ForeignKey(User)
