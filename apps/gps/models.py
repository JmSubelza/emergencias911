# encoding:utf-8
from django.db import models


# Create your models here.
class Device(models.Model):
    color = models.CharField(null=True, max_length=255)
    imei = models.CharField(max_length=255, unique=True, null=True, verbose_name='Número de IMEI')
    mail_drop_alarm = models.CharField(max_length=255, null=True)
    modification_date = models.DateTimeField(null=True, verbose_name='Tiempo')
    name = models.CharField(max_length=100, unique=True, null=True, verbose_name='Nombre Dispositivo')
    phone_number = models.CharField(max_length=100, null=True, verbose_name='Número de SIM')
    status = models.CharField(max_length=255, null=True)

    lat = models.FloatField(null=True, verbose_name='Latitud')
    lng = models.FloatField(null=True, verbose_name='Longitud')
    time = models.DateTimeField(verbose_name='Tiempo', null=True)

    is_active = models.BooleanField(verbose_name='Activo', default=True)

    def __str__(self):
        return '{}'.format(self.name)


class Positions_Buffer(models.Model):
    altitude = models.FloatField(null=True, verbose_name='Altitud')
    battery = models.CharField(max_length=255, null=True)
    command = models.CharField(max_length=255, null=True)
    course = models.FloatField(null=True)
    extended_info = models.TextField(null=True)
    latitude = models.FloatField(null=True, verbose_name='Latitud')
    longitude = models.FloatField(null=True, verbose_name='Longitud')
    sent_date = models.DateTimeField(null=True)
    speed = models.FloatField(null=True, verbose_name='Velocidad')
    time = models.DateTimeField(null=True)
    valid = models.BooleanField(default=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    accuracy = models.FloatField(null=True)


class Positions(models.Model):
    altitude = models.FloatField(null=True, verbose_name='Altitud')
    battery = models.CharField(max_length=255, null=True)
    command = models.CharField(max_length=255, null=True)
    course = models.FloatField(null=True)
    extended_info = models.TextField(null=True)
    latitude = models.FloatField(null=True, verbose_name='Latitud')
    longitude = models.FloatField(null=True, verbose_name='Longitud')
    sent_date = models.DateTimeField(null=True)
    speed = models.FloatField(null=True, verbose_name='Velocidad')
    time = models.DateTimeField(null=True)
    valid = models.BooleanField(default=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    accuracy = models.FloatField(null=True)


class Plots(models.Model):
    port = models.IntegerField(null=True)
    command = models.CharField(max_length=500, null=True)
    sent_date = models.DateTimeField(null=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)


class Alarm(models.Model):
    battery = models.IntegerField(null=True)
    date_received = models.DateTimeField(null=True)
    date_sent = models.DateTimeField(null=True)
    device_id = models.BigIntegerField(null=True)
    is_sent = models.BooleanField(default=True)
    latitude = models.FloatField(null=True, verbose_name='Latitud')
    longitude = models.FloatField(null=True, verbose_name='Longitud')
    speed = models.FloatField(null=True, verbose_name='Velocidad')
    type = models.CharField(max_length=255, null=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
