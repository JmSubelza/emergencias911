from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from apps.logistica.views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete, \
    TipoIncidenteCreate, TipoIncidenteList, TipoIncidenteUpdate, TipoIncidenteDelete, \
    AsignacionIncidenteCreate, AsignacionIncidenteList, AsignacionIncidenteUpdate, AsignacionIncidenteDelete, \
    MapaIncidente, MapaCentroEmergencia

urlpatterns = [

    url(r'^incidente/$', IncidenteList.as_view(), name='incidente'),
    url(r'^incidente/nuevo/$', IncidenteCreate.as_view(), name='incidente_crear'),
    url(r'^incidente/editar/(?P<pk>\d+)/$', IncidenteUpdate.as_view(), name='incidente_editar'),
    url(r'^incidente/eliminar/(?P<pk>\d+)/$', IncidenteDelete.as_view(), name='incidente_eliminar'),

    url(r'^tipoincidente/$', TipoIncidenteList.as_view(), name='tipo_incidente'),
    url(r'^tipoincidente/nuevo/$', TipoIncidenteCreate.as_view(), name='tipo_incidente_crear'),
    url(r'^tipoincidente/editar/(?P<pk>\d+)/$', TipoIncidenteUpdate.as_view(), name='tipo_incidente_editar'),
    url(r'^tipoincidente/eliminar/(?P<pk>\d+)/$', TipoIncidenteDelete.as_view(), name='tipo_incidente_eliminar'),

    url(r'^asignacionincidente/$', AsignacionIncidenteList.as_view(), name='asignacion_incidente'),
    url(r'^asignacionincidente/nuevo/$', AsignacionIncidenteCreate.as_view(), name='asignacion_incidente_crear'),
    url(r'^asignacionincidente/editar/(?P<pk>\d+)/$', AsignacionIncidenteUpdate.as_view(),
        name='asignacion_incidente_editar'),
    url(r'^asignacionincidente/eliminar/(?P<pk>\d+)/$', AsignacionIncidenteDelete.as_view(),
        name='asignacion_incidente_eliminar'),

    url(r'^mapaincidente/$', MapaIncidente.as_view(), name='mapa_incidente'),
    url(r'^mapacentroemergencia/$', MapaCentroEmergencia.as_view(), name='mapa_centroemergencia'),

]

