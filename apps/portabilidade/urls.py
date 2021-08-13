from django.urls import path
from .views import Index
from .views import CadastrarPortabilidade

urlpatterns = [
    path('a/', Index),

    path('cadastrar-portabilidade/', CadastrarPortabilidade.as_view(), name='cadastrar-portabilidade'),
]