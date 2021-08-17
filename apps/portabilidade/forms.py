from django import forms
from .models import Portabilidade

class PortabilidadeCreateForm(forms.ModelForm):
    class Meta:
        model = Portabilidade
        fields = ['nome_razao_social',
                  'cpf',
                  'cep',
                  'cidade',
                  'uf',
                  'logradouro',
                  'bairro',
                  'numero',
                  'documento',
                  'fatura',
                  'numero_portar',

                  ]