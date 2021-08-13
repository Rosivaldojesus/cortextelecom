from django.shortcuts import render
from .models import Portabilidade
from .forms import PortabilidadeCreateForm
from django.views.generic.edit import CreateView

# Create your views here.

def Index(request):
    return render(request, 'portabilidade/index.html')


class CadastrarPortabilidade(CreateView):
    model = Portabilidade
    form_class = PortabilidadeCreateForm
    success_url = '/'
    template_name = 'portabilidade/cadastrar-portabilidade.html'
