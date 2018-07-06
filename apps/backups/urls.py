from django.conf.urls import url
from .views import BackupView

urlpatterns = [
    url(r'^download/$', BackupView.as_view(), name="backups_view"),
]