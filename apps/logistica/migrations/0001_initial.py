# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionIncidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tiempo')),
                ('estado', models.CharField(choices=[('EN CURSO', 'EN CURSO (ASIGNADO)'), ('RESULTO', 'RESUELTO'), ('FINALIZADO', 'FINALIZADO')], default='EN CURSO', max_length=20, verbose_name='Estado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('centro_emergencia', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='servicios.CentroEmergencia')),
            ],
        ),
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Tiempo')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('NUEVO', 'NUEVO'), ('EN CURSO', 'EN CURSO (ASIGNADO)'), ('RESULTO', 'RESUELTO'), ('FINALIZADO', 'FINALIZADO')], default='NUEVO', max_length=20, verbose_name='Estado')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=100, verbose_name='Latitud')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=100, verbose_name='Longitud')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
        ),
        migrations.AddField(
            model_name='incidente',
            name='tipo',
            field=models.ManyToManyField(to='logistica.TipoIncidente'),
        ),
        migrations.AddField(
            model_name='incidente',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='asignacionincidente',
            name='incidente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='logistica.Incidente'),
        ),
        migrations.AddField(
            model_name='asignacionincidente',
            name='vehiculos',
            field=models.ManyToManyField(to='servicios.Vehiculo'),
        ),
    ]
