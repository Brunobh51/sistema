from django.db import models
from models import Cliente


def salvar_dados_cliente(nome, telefone, endereco, valor_pedido, valor_boy, pedido_pago, motoboy_pago, descricao):
    cliente = Cliente(
        nome=nome,
        telefone=telefone,
        endereco=endereco,
        valor_pedido=valor_pedido,
        valor_boy=valor_boy,
        pedido_pago=pedido_pago,
        motoboy_pago=motoboy_pago,
        descricao=descricao
    )
    cliente.save()
    return ('ok')
