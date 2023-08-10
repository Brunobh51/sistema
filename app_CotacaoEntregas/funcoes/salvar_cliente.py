def criar_cliente(request):
    valorboy = request.POST.get('valormotoboy')
    nome = request.POST.get('nome_cliente')
    telefone = request.POST.get('telefone')
    cep = request.POST.get('cep_cliente')
    rua = request.POST.get('rua_cliente')
    bairro = request.POST.get('bairro_cliente')
    cidade = request.POST.get('cidade_cliente')
    numero = request.POST.get('numero_cliente')
    complemento = request.POST.get('complemento_cliente')
    valor_pedido = request.POST.get('valor_pedido')
    informacoes_adicionais = request.POST.get(
        'exampleFormControlTextarea1')
    pedido_pago = request.POST.get('pedido_pago')
    motoboy_pago = request.POST.get('motoboy_pago')

    # Crie uma instância do modelo Cliente
    novo_cliente = Cliente(
        nome=nome,
        telefone=telefone,
        endereco=f'{cep}, {rua}, {bairro}, {cidade}, {numero}',
        valor_pedido=valor_pedido,
        valor_boy=valorboy,
        descricao=informacoes_adicionais,
        pedido_pago=pedido_pago,
        motoboy_pago=motoboy_pago,
    )

    # Salve o cliente no banco de dados
    novo_cliente.save()
    print(motoboy_pago)