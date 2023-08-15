from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=True, null=True)
    n_pedido = models.CharField(max_length=200, verbose_name='Nº Pedido', blank=True, null=True)
    telefone = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Pedido', blank=True, null=True)
    valor_boy = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Boy', blank=True, null=True)
    pedido_pago = models.BooleanField(default=False, verbose_name='Pedido Pago', blank=True, null=True)
    motoboy_pago = models.BooleanField(default=False, verbose_name='Motoboy Pago', blank=True, null=True)
    descricao = models.TextField(verbose_name='Informações adicionais', blank=True, null=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=200, verbose_name='Rua', blank=True, null=True)
    numero = models.CharField(max_length=10, verbose_name='Numero', blank=True, null=True)
    bairro = models.CharField(max_length=100, verbose_name='Bairro', blank=True, null=True)
    cidade = models.CharField(max_length=200, verbose_name='Cidade', blank=True, null=True)
    estado = models.CharField(max_length=20, verbose_name='UF', blank=True, null=True)
    cep = models.CharField(max_length=9, verbose_name='Cep', blank=True, null=True)
    complemento = models.CharField(max_length=200, verbose_name='Complemento', blank=True, null=True)

    

    def __str__(self):
        return self.cidade

    class Meta:
        verbose_name_plural = 'Endereços'
        db_table = 'endereco'
