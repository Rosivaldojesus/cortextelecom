# Generated by Django 3.0 on 2021-08-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portabiliade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=15)),
                ('cep', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=20)),
                ('documento', models.FileField(blank=True, null=True, upload_to='documento_imagens/%Y/%m')),
                ('fatura', models.FileField(blank=True, null=True, upload_to='fatura_imagens/%Y/%m')),
            ],
            options={
                'verbose_name': 'Portabilidade',
                'verbose_name_plural': 'Portabilidades',
            },
        ),
    ]