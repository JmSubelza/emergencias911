from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.administracion.forms import UserForm
# Create your views here.

class UsuarioCreate(CreateView):
    model = User
    template_name = 'administracion/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:user')


