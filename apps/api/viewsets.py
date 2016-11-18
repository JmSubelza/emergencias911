from django.contrib.auth.models import User, Group
from apps.api.serializers import UserSerializer, GroupSerializer, TipoIncidenteSerializer
from apps.logistica.models import TipoIncidente
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('pk')
    serializer_class = GroupSerializer


class TipoIncidenteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoIncidente.objects.all()
    serializer_class = TipoIncidenteSerializer
