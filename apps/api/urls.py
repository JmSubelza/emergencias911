from django.conf.urls import url

from apps.api.viewsets import UserViewSet

urlpatterns = [

    url(r'^usuario/$', UserViewSet(), name='api.usuario'),

]
