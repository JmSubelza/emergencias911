from django.conf.urls import url
from apps.logistica.views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete

urlpatterns = [

    url(r'^incidente$', IncidenteList.as_view(), name='incidente'),
    url(r'^incidente/nuevo/$', IncidenteCreate.as_view(), name='inicidente_crear'),
    url(r'^incidente/editar/(?P<pk>\d+)/$', IncidenteUpdate.as_view(), name='incidente_editar'),
    url(r'^incidente/eliminar/(?P<pk>\d+)/$', IncidenteDelete.as_view(), name='vehiculo_eliminar'),

    ]