from django.contrib import admin
from .models import CentroEmergencia, TipoVehiculo, Vehiculo, Device

# Register your models here.

admin.site.register(CentroEmergencia)
admin.site.register(TipoVehiculo)
admin.site.register(Vehiculo)
