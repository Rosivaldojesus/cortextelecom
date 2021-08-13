from django.db import models


# Create your models here.
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

    class Meta:
        verbose_name = "Portabilidade"
        verbose_name_plural = "Portabilidades"

    def __str__(self):
        return "{}".format(self.nome_razao_social)

