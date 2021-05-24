# from django.conf.urls import url
from django.urls import path

from apps.api.viewsets import UserViewSet

app_name = 'api'

urlpatterns = [

    path('usuario/', UserViewSet(), name='api.usuario'),

]
