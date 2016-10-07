from django.conf.urls import url
from apps.administracion.views import UsuarioCreate

urlpatterns = [

    url(r'^usuario/nuevo$', UsuarioCreate.as_view(), name='usuario_crear'),

]