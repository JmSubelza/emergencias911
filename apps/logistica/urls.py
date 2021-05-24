# encoding:utf-8
from django.conf.urls import url
from django.urls import path
from .views import \
    IncidenteCreate, IncidenteList, IncidenteUpdate, IncidenteDelete, IncidenteDetail, \
    TipoIncidenteCreate, TipoIncidenteList, TipoIncidenteUpdate, TipoIncidenteDelete, TipoIncidenteDetail, \
    AsignacionIncidenteCreate, AsignacionIncidenteList, AsignacionIncidenteUpdate, AsignacionIncidenteDelete, \
    AsignacionIncidenteDetail, \
    MapaIncidente, MapaCentroEmergencia, MapaVehiculo

app_name = 'logistica'

urlpatterns = [

    path('incidente/', IncidenteList.as_view(), name='incidente'),
    path('incidente/nuevo/', IncidenteCreate.as_view(), name='incidente_crear'),
    path('incidente/editar/<int:pk>/', IncidenteUpdate.as_view(), name='incidente_editar'),
    path('incidente/delete/<int:pk>/', IncidenteDelete.as_view(), name='incidente_eliminar'),
    path('incidente/view/<int:pk>/', IncidenteDetail.as_view(), name='incidente_detalle'),

    path('tipoincidente/', TipoIncidenteList.as_view(), name='tipo_incidente'),
    path('tipoincidente/nuevo/', TipoIncidenteCreate.as_view(), name='tipo_incidente_crear'),
    path('tipoincidente/editar/<int:pk>/', TipoIncidenteUpdate.as_view(), name='tipo_incidente_editar'),
    path('tipoincidente/delete/<int:pk>/', TipoIncidenteDelete.as_view(), name='tipo_incidente_eliminar'),
    path('tipoincidente/view/<int:pk>/', TipoIncidenteDetail.as_view(), name='tipo_incidente_detalle'),

    path('asignacionincidente/', AsignacionIncidenteList.as_view(), name='asignacion_incidente'),
    path('asignacionincidente/nuevo/', AsignacionIncidenteCreate.as_view(), name='asignacion_incidente_crear'),
    path('asignacionincidente/editar/<int:pk>/', AsignacionIncidenteUpdate.as_view(),
         name='asignacion_incidente_editar'),
    path('asignacionincidente/delete/<int:pk>/', AsignacionIncidenteDelete.as_view(),
         name='asignacion_incidente_eliminar'),
    path('asignacionincidente/view/<int:pk>/', AsignacionIncidenteDetail.as_view(),
         name='asignacion_incidente_detalle'),

    path('mapaincidente/', MapaIncidente.as_view(), name='mapa_incidente'),
    path('mapacentroemergencia/', MapaCentroEmergencia.as_view(), name='mapa_centroemergencia'),
    path('mapavehiculo/', MapaVehiculo.as_view(), name='mapa_vehiculo'),

]
