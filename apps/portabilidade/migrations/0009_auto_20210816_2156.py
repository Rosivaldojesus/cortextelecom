# Generated by Django 3.0 on 2021-08-17 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portabilidade', '0008_auto_20210816_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portabilidade',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='portabilidade.StatusPortabilidade'),
        ),
    ]
