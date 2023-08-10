# Generated by Django 4.2.4 on 2023-08-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Nome"
                    ),
                ),
                (
                    "telefone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "endereco",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Endereço"
                    ),
                ),
                (
                    "valor_pedido",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Valor do Pedido",
                    ),
                ),
                (
                    "valor_boy",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Valor do Boy",
                    ),
                ),
                (
                    "pedido_pago",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="Pedido Pago"
                    ),
                ),
                (
                    "motoboy_pago",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        null=True,
                        verbose_name="Motoboy Pago",
                    ),
                ),
                (
                    "descricao",
                    models.TextField(blank=True, null=True, verbose_name="Descrição"),
                ),
            ],
            options={
                "verbose_name_plural": "Clientes",
                "db_table": "cliente",
            },
        ),
    ]
