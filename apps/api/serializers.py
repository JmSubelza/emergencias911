from django.contrib.auth.models import User, Group

from rest_framework.serializers import ModelSerializer

from ..logistica.models import TipoIncidente, Incidente, AsignacionIncidente

from ..servicios.models import CentroEmergencia, TipoVehiculo, Vehiculo, DispositivoGPS


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class UserSerializer(ModelSerializer):
    groups = GroupSerializer(many=True, read_only=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'groups', 'is_active')


class CentroEmergenciaSerializer(ModelSerializer):
    class Meta:
        model = CentroEmergencia
        fields = ('__all__')


class DispositivoGPSSerializer(ModelSerializer):
    class Meta:
        model = DispositivoGPS
        fields = ('__all__')


class TipoVehiculoSerializer(ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ('__all__')


class VehiculoSerializer(ModelSerializer):
    tipo_id = TipoVehiculoSerializer(many=False, read_only=False)
    gps_id = DispositivoGPSSerializer(many=False, read_only=False)

    class Meta:
        model = Vehiculo
        fields = (
            'id', 'placa', 'name', 'marca', 'modelo', 'nro_motor', 'nro_chasis', 'sector', 'tipo_id', 'gps_id',
            'is_active')


class TipoIncidenteSerializer(ModelSerializer):
    class Meta:
        model = TipoIncidente
        fields = ('__all__')


class IncidenteSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=False)
    tipo = TipoIncidenteSerializer(many=True, read_only=False)

    class Meta:
        model = Incidente
        fields = ('id', 'time', 'descripcion', 'lat', 'lng', 'estado', 'user', 'tipo', 'is_active')


class AsignacionIncidenteSerializer(ModelSerializer):
    incidente = IncidenteSerializer(many=False, read_only=False)
    centro_emergencia = CentroEmergenciaSerializer(many=False)

    class Meta:
        model = AsignacionIncidente
        fields = ('id', 'time', 'incidente', 'centro_emergencia', 'vehiculos', 'estado', 'is_active')
