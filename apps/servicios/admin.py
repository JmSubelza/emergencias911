from django.contrib import admin
from .models import CentroEmergencia, TipoVehiculo, Vehiculo, DispositivoGPS

# Register your models here.

admin.site.register(CentroEmergencia)
admin.site.register(TipoVehiculo)
admin.site.register(Vehiculo)
admin.site.register(DispositivoGPS)
