# encoding:utf-8
from django.conf.urls import url
from .views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete, IncidenteDetail, \
    TipoIncidenteCreate, TipoIncidenteList, TipoIncidenteUpdate, TipoIncidenteDelete, TipoIncidenteDetail, \
    AsignacionIncidenteCreate, AsignacionIncidenteList, AsignacionIncidenteUpdate, AsignacionIncidenteDelete, \
    AsignacionIncidenteDetail, \
    MapaIncidente, MapaCentroEmergencia, MapaVehiculo

urlpatterns = [

    url(r'^incidente/$', IncidenteList.as_view(), name='incidente'),
    url(r'^incidente/nuevo/$', IncidenteCreate.as_view(), name='incidente_crear'),
    url(r'^incidente/editar/(?P<pk>\d+)/$', IncidenteUpdate.as_view(), name='incidente_editar'),
    url(r'^incidente/delete/(?P<pk>\d+)/$', IncidenteDelete.as_view(), name='incidente_eliminar'),
    url(r'^incidente/view/(?P<pk>\d+)/$', IncidenteDetail.as_view(), name='incidente_detalle'),

    url(r'^tipoincidente/$', TipoIncidenteList.as_view(), name='tipo_incidente'),
    url(r'^tipoincidente/nuevo/$', TipoIncidenteCreate.as_view(), name='tipo_incidente_crear'),
    url(r'^tipoincidente/editar/(?P<pk>\d+)/$', TipoIncidenteUpdate.as_view(),
        name='tipo_incidente_editar'),
    url(r'^tipoincidente/delete/(?P<pk>\d+)/$', TipoIncidenteDelete.as_view(),
        name='tipo_incidente_eliminar'),
    url(r'^tipoincidente/view/(?P<pk>\d+)/$', TipoIncidenteDetail.as_view(),
        name='tipo_incidente_detalle'),

    url(r'^asignacionincidente/$', AsignacionIncidenteList.as_view(), name='asignacion_incidente'),
    url(r'^asignacionincidente/nuevo/$', AsignacionIncidenteCreate.as_view(),
        name='asignacion_incidente_crear'),
    url(r'^asignacionincidente/editar/(?P<pk>\d+)/$', AsignacionIncidenteUpdate.as_view(),
        name='asignacion_incidente_editar'),
    url(r'^asignacionincidente/delete/(?P<pk>\d+)/$', AsignacionIncidenteDelete.as_view(),
        name='asignacion_incidente_eliminar'),
    url(r'^asignacionincidente/view/(?P<pk>\d+)/$', AsignacionIncidenteDetail.as_view(),
        name='asignacion_incidente_detalle'),

    url(r'^mapaincidente/$', MapaIncidente.as_view(), name='mapa_incidente'),
    url(r'^mapacentroemergencia/$', MapaCentroEmergencia.as_view(), name='mapa_centroemergencia'),
    url(r'^mapavehiculo/$', MapaVehiculo.as_view(), name='mapa_vehiculo'),

]
