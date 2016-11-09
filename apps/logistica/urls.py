from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.logistica.views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete, IncidenteDetail, \
    TipoIncidenteCreate, TipoIncidenteList, TipoIncidenteUpdate, TipoIncidenteDelete, TipoIncidenteDetail, \
    AsignacionIncidenteCreate, AsignacionIncidenteList, AsignacionIncidenteUpdate, AsignacionIncidenteDelete, \
    AsignacionIncidenteDetail, \
    MapaIncidente, MapaCentroEmergencia, MapaVehiculo

urlpatterns = [

    url(r'^incidente/$', login_required(IncidenteList.as_view()), name='incidente'),
    url(r'^incidente/nuevo/$', login_required(IncidenteCreate.as_view()), name='incidente_crear'),
    url(r'^incidente/editar/(?P<pk>\d+)/$', login_required(IncidenteUpdate.as_view()), name='incidente_editar'),
    url(r'^incidente/eliminar/(?P<pk>\d+)/$', login_required(IncidenteDelete.as_view()), name='incidente_eliminar'),
    url(r'^incidente/detalle/(?P<pk>\d+)/$', login_required(IncidenteDetail.as_view()), name='incidente_detalle'),

    url(r'^tipoincidente/$', login_required(TipoIncidenteList.as_view()), name='tipo_incidente'),
    url(r'^tipoincidente/nuevo/$', login_required(TipoIncidenteCreate.as_view()), name='tipo_incidente_crear'),
    url(r'^tipoincidente/editar/(?P<pk>\d+)/$', login_required(TipoIncidenteUpdate.as_view()),
        name='tipo_incidente_editar'),
    url(r'^tipoincidente/eliminar/(?P<pk>\d+)/$', login_required(TipoIncidenteDelete.as_view()),
        name='tipo_incidente_eliminar'),
    url(r'^tipoincidente/detalle/(?P<pk>\d+)/$', login_required(TipoIncidenteDetail.as_view()),
        name='tipo_incidente_detalle'),

    url(r'^asignacionincidente/$', login_required(AsignacionIncidenteList.as_view()), name='asignacion_incidente'),
    url(r'^asignacionincidente/nuevo/$', login_required(AsignacionIncidenteCreate.as_view()),
        name='asignacion_incidente_crear'),
    url(r'^asignacionincidente/editar/(?P<pk>\d+)/$', login_required(AsignacionIncidenteUpdate.as_view()),
        name='asignacion_incidente_editar'),
    url(r'^asignacionincidente/eliminar/(?P<pk>\d+)/$', login_required(AsignacionIncidenteDelete.as_view()),
        name='asignacion_incidente_eliminar'),
    url(r'^asignacionincidente/detalle/(?P<pk>\d+)/$', login_required(AsignacionIncidenteDetail.as_view()),
        name='asignacion_incidente_detalle'),

    url(r'^mapaincidente/$', login_required(MapaIncidente.as_view()), name='mapa_incidente'),
    url(r'^mapacentroemergencia/$', login_required(MapaCentroEmergencia.as_view()), name='mapa_centroemergencia'),
    url(r'^mapavehiculo/$', login_required(MapaVehiculo.as_view()), name='mapa_vehiculo'),

]
