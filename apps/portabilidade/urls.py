from django.urls import path
from .views import Index
from .views import CadastrarPortabilidade, PedidoPortabilidade, PedidoVisualizacao, PedidoEditar

urlpatterns = [
    path('', Index),
    path('pedido-portabilidade/', PedidoPortabilidade),
    path('pedido-portabilidade/visualizar-portabilidade/', PedidoVisualizacao),
    path('editar-portabilidade/<int:id>', PedidoEditar),

    path('cadastrar-portabilidade/', CadastrarPortabilidade.as_view(), name='cadastrar-portabilidade'),


]