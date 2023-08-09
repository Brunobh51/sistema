from app_CotacaoEntregas.models import Cliente


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


print(salvar_dados_cliente('Bruno', '32124812', 'rua x ', '12,50',
                           '12,00', 'sim', 'sim', 'teste'))
