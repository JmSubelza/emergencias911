from django.conf.urls import url
from django.urls import path
from .views import \
    DispositivoGpsList, DispositivoGpsCreate, DispositivoGpsUpdate, DispositivoGpsDelete, DispositivoGpsDetail

app_name = 'gps'

urlpatterns = [
    path('dispositivogps/', DispositivoGpsList.as_view(), name='dispositivo_gps'),
    path('dispositivogps/nuevo/', DispositivoGpsCreate.as_view(), name='dispositivo_gps_crear'),
    path('dispositivogps/editar/<int:pk>/', DispositivoGpsUpdate.as_view(), name='dispositivo_gps_editar'),
    path('dispositivogps/delete/<int:pk>/', DispositivoGpsDelete.as_view(), name='dispositivo_gps_eliminar'),
    path('dispositivogps/view/<int:pk>/', DispositivoGpsDetail.as_view(), name='dispositivo_gps_detalle'),

]
