from django.contrib.auth.models import User, Group

from .serializers import UserSerializer, GroupSerializer, TipoIncidenteSerializer, IncidenteSerializer, \
    AsignacionIncidenteSerializer, CentroEmergenciaSerializer, TipoVehiculoSerializer, VehiculoSerializer, \
    DispositivoGPSSerializer
from ..logistica.models import TipoIncidente, Incidente, AsignacionIncidente
from rest_framework.viewsets import ModelViewSet

from ..servicios.models import CentroEmergencia, TipoVehiculo, Vehiculo, DispositivoGPS


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by('pk')
    serializer_class = GroupSerializer


class CentroEmergenciaViewSet(ModelViewSet):
    queryset = CentroEmergencia.objects.all().order_by('pk')
    serializer_class = CentroEmergenciaSerializer


class DispositivoGPSViewSet(ModelViewSet):
    queryset = DispositivoGPS.objects.all().order_by('pk')
    serializer_class = DispositivoGPSSerializer


class TipoVehiculoViewSet(ModelViewSet):
    queryset = TipoVehiculo.objects.all().order_by('pk')
    serializer_class = TipoVehiculoSerializer


class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all().order_by('pk')
    serializer_class = VehiculoSerializer


class TipoIncidenteViewSet(ModelViewSet):
    queryset = TipoIncidente.objects.all().order_by('pk')
    serializer_class = TipoIncidenteSerializer


class IncidenteViewSet(ModelViewSet):
    queryset = Incidente.objects.all().order_by('-pk')
    serializer_class = IncidenteSerializer


class AsignacionIncidenteViewSet(ModelViewSet):
    queryset = AsignacionIncidente.objects.all().order_by('-pk')
    serializer_class = AsignacionIncidenteSerializer
