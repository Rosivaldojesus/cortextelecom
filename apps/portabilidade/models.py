from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class StatusPortabilidade(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Status da Portabilidade"

    def __str__(self):
        return "{}".format(self.status)



class Portabilidade(models.Model):
    nome_razao_social = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    cep = models.CharField(max_length=20)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    documento = models.FileField(
        upload_to='documento_imagens/%Y/%m', blank=True, null=True)
    fatura = models.FileField(
        upload_to='fatura_imagens/%Y/%m', blank=True, null=True)
    numero_portar = models.CharField(max_length=100)
    numero_sip = models.CharField(max_length=10)
    solicitante = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                                  related_name='solicitante', blank=True, null=True)
    data_solicitacao =  models.DateTimeField(auto_now=True)
    data_conclusao = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(StatusPortabilidade, on_delete=models.CASCADE, default=2, blank=True, null=True)


    class Meta:
        verbose_name = "Portabilidade"
        verbose_name_plural = "Portabilidades"

    def __str__(self):
        return "{}".format(self.nome_razao_social)

