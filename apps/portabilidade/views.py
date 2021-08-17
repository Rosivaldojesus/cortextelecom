from django.shortcuts import render, redirect, get_object_or_404
from .models import Portabilidade
from .forms import PortabilidadeCreateForm
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.
def Index(request):
    return render(request, 'portabilidade/index.html')


class CadastrarPortabilidade(CreateView):
    model = Portabilidade
    form_class = PortabilidadeCreateForm
    success_url = '/'
    template_name = 'portabilidade/cadastrar-portabilidade.html'

    def form_valid(self, form):
        form.instance.solicitante = self.request.user
        return super(CadastrarPortabilidade, self).form_valid(form)


def PedidoPortabilidade(request):
    pedidos = Portabilidade.objects.all()
    return render(request, 'portabilidade/pedido-portabilidade.html', {'pedidos':pedidos} )


def PedidoVisualizacao(request):
    pedido = request.GET.get('id')
    if pedido:
        pedido = Portabilidade.objects.get(id=pedido)
    return render(request, 'portabilidade/visualizar-pedido.html',{'pedido': pedido})


def PedidoEditar(request, id=None):
    pedido = get_object_or_404(Portabilidade, id=id)
    form = PortabilidadeCreateForm(request.POST or None, instance=pedido)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Portabiliade editada com sucesso!!!.')
        return redirect('/portabilidade/')
    return render(request, 'portabilidade/editar-portabilidade.html', {'form': form})