from django.db import models


class Cliente(models.Model):
    nome = models.CharField(
        max_length=100, verbose_name='Nome', blank=True, null=True)
    telefone = models.CharField(
        max_length=20, verbose_name='Telefone', blank=True, null=True)
    endereco = models.CharField(
        max_length=200, verbose_name='Endereço', blank=True, null=True)
    valor_pedido = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor do Pedido', blank=True, null=True)
    valor_boy = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor do Boy', blank=True, null=True)
    pedido_pago = models.BooleanField(
        default=False, verbose_name='Pedido Pago', blank=True, null=True)
    motoboy_pago = models.BooleanField(
        default=False, verbose_name='Motoboy Pago', blank=True, null=True)
    descricao = models.TextField(
        verbose_name='Descrição', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
