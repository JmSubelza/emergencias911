# from django.conf.urls import url
from django.urls import path
from .views import \
    UsuarioList, UsuarioCreate, UsuarioUpdate, UsuarioDelete, UsuarioDetail, \
    GrupoCreate, GrupoList, GrupoUpdate, GrupoDelete, GrupoDetail

app_name = 'administracion'

urlpatterns = [

    path('usuario/', UsuarioList.as_view(), name='usuario'),
    path('usuario/nuevo/', UsuarioCreate.as_view(), name='usuario_crear'),
    path('usuario/editar/<int:pk>/', UsuarioUpdate.as_view(), name='usuario_editar'),
    path('usuario/delete/<int:pk>/', UsuarioDelete.as_view(), name='usuario_eliminar'),
    path('usuario/view/<int:pk>/', UsuarioDetail.as_view(), name='usuario_detalle'),

    path('grupo/', GrupoList.as_view(), name='grupo'),
    path('grupo/nuevo/', GrupoCreate.as_view(), name='grupo_crear'),
    path('grupo/editar/<int:pk>/', GrupoUpdate.as_view(), name='grupo_editar'),
    path('grupo/delete/<int:pk>/', GrupoDelete.as_view(), name='grupo_eliminar'),
    path('grupo/view/<int:pk>/', GrupoDetail.as_view(), name='grupo_detalle'),

]
