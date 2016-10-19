from django.db import models
from apps.servicios.models import CentroEmergencia, Vehiculo
from django.contrib.auth.models import User


# Create your models here.


class TipoIncidente(models.Model):
    name = models.CharField(max_length=100, verbose_name='Descripción')
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Incidente(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Tiempo', null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=100)
    descripcion = models.TextField()
    ESTADO = (
        ('NUEVO', 'NUEVO'),
        ('EN CURSO', 'EN CURSO (ASIGNADO)'),
        ('RESULTO', 'RESUELTO'),
        ('FINALIZADO', 'FINALIZADO'),
    )
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO, default='NUEVO')
    lat = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    log = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    is_active = models.BooleanField(verbose_name='Activo', default=True)
    tipo = models.ManyToManyField(TipoIncidente)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{}'.format(self.id)

    def get_string_tipo(self):
        return ', '.join([tipos.name for tipos in self.tipo.all()])


class AsignacionIncidente(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Tiempo', null=True)
    ESTADO = (
        ('EN CURSO', 'EN CURSO (ASIGNADO)'),
        ('RESULTO', 'RESUELTO'),
        ('FINALIZADO', 'FINALIZADO'),
    )
    estado = models.CharField(verbose_name='Estado', max_length=20, choices=ESTADO, default='EN CURSO')
    incidente = models.OneToOneField(Incidente)
    centro_emergencia = models.ForeignKey(CentroEmergencia, blank=True)
    vehiculos = models.ManyToManyField(Vehiculo)
    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_string_vehiculos(self):
        return ', '.join([vehiculo.placa for vehiculo in self.vehiculos.all()])
