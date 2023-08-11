from app_CotacaoEntregas.models import Cliente,Endereco

def criar_cliente(nome, n_pedido, telefone, valor_pedido, valor_boy, pedido_pago, motoboy_pago, descricao, rua, numero, bairro, cidade, estado):
    cliente = Cliente.objects.create(
        nome=nome,
        n_pedido=n_pedido,
        telefone=telefone,
        valor_pedido=valor_pedido,
        valor_boy=valor_boy,
        pedido_pago=pedido_pago,
        motoboy_pago=motoboy_pago,
        descricao=descricao
    )
    endereco = Endereco.objects.create(
        cliente=cliente,
        rua=rua,
        numero=numero,
        bairro=bairro,
        cidade=cidade,
        estado=estado
    )
    return cliente, endereco

