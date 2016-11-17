from apps.logistica.models import TipoIncidente
from rest_framework import viewsets
from apps.logistica.serializers import TipoIncidenteSerializer


class TipoIncidenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoIncidente.objects.all()
    serializer_class = TipoIncidenteSerializer