# Generated by Django 4.2.4 on 2023-08-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_CotacaoEntregas', '0003_alter_cliente_n_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cep'),
        ),
    ]
