from apps.logistica.models import TipoIncidente
from rest_framework import serializers


class TipoIncidenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoIncidente
        fields = ('url', 'name')
