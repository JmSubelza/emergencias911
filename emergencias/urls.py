"""emergencias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^servicios/', include('apps.servicios.urls', namespace="servicios")),
                  url(r'^administracion/', include('apps.administracion.urls', namespace="administracion")),
                  url(r'^logistica/', include('apps.logistica.urls', namespace="logistica")),
                  url(r'^accounts/login/$', login, {'template_name': 'index.html'}, name='login'),
                  url(r'^logout/$', logout_then_login, name='logout'),
                  url(r'^reset/password_reset/$', password_reset,
                      {'template_name': 'registro/password_reset_form.html',
                       'email_template_name': 'registro/password_reset_email.html'},
                      name='password_reset'),
                  url(r'^reset/password_reset_done/$', password_reset_done,
                      {'template_name': 'registro/password_reset_done.html'},
                      name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
                      {'template_name': 'registro/password_reset_confirm.html'},
                      name='password_reset_confirm'
                      ),
                  url(r'^reset/done/$', password_reset_complete,
                      {'template_name': 'registro/password_reset_complete.html'},
                      name='password_reset_complete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
