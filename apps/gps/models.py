# encoding:utf-8
from django.db import models


# Create your models here.
class Device(models.Model):
    color = models.CharField(max_length=255)
    imei = models.IntegerField(unique=True, verbose_name='Número de IMEI')
    mail_drop_alarm = models.CharField(max_length=255)
    modification_date = models.DateTimeField(verbose_name='Tiempo', null=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre Dispositivo')
    phone_number = models.CharField(max_length=100, verbose_name='Número de SIM')
    status = models.CharField(max_length=255)

    lat = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    lng = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    time = models.DateTimeField(verbose_name='Tiempo', null=True)

    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Positions_Buffer(models.Model):
    altitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Altitud')
    battery = models.CharField(max_length=255, null=True, blank=True)
    command = models.CharField(max_length=255, null=True, blank=True)
    course = models.DecimalField(max_digits=100, decimal_places=6)
    extended_info = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    longitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    sent_date = models.DateTimeField(null=True)
    speed = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Velocidad')
    time = models.DateTimeField(null=True)
    valid = models.BooleanField(default=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    accuracy = models.DecimalField(max_digits=100, decimal_places=6)


class Positions(models.Model):
    altitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Altitud')
    battery = models.CharField(max_length=255, null=True, blank=True)
    command = models.CharField(max_length=255, null=True, blank=True)
    course = models.DecimalField(max_digits=100, decimal_places=6)
    extended_info = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    longitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    sent_date = models.DateTimeField(null=True)
    speed = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Velocidad')
    time = models.DateTimeField(null=True)
    valid = models.BooleanField(default=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    accuracy = models.DecimalField(max_digits=100, decimal_places=6)


class Plots(models.Model):
    port = models.IntegerField(null=True)
    command = models.CharField(max_length=500, null=True, blank=True)
    sent_date = models.DateTimeField(null=True)

class Alarm(models.Model):
    battery = models.IntegerField()
    date_received = models.DateTimeField(null=True)
    date_sent = models.DateTimeField(null=True)
    device_id = models.BigIntegerField()
    is_sent = models.BinaryField(default=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Latitud')
    longitude = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Longitud')
    speed = models.DecimalField(max_digits=100, decimal_places=6, verbose_name='Velocidad')
    type = models.CharField(max_length=255, null=True, blank=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)



