from django.shortcuts import render
from .funcoes.cep import consultar_cep
from .funcoes.correio import valor_correio
from .funcoes.motoboy_borzo import valor_motoboy
from .models import Cliente


def dashboard(request):
    return render(request, 'dashboard.html')


def cotacao(request):
    if request.method == "POST":
        cep = request.POST.get('cep')
        content = consultar_cep(cep)
        if cep == '':
            context = {'erro': 'Favor digitar um cep para continuar'}
            return render(request, 'app_CotacaoEntregas/cotacao.html', context)

        if content and not content.get('erro'):
            peso = request.POST.get('peso')
            valores = valor_correio(content['cep'], peso)
            valormotoboy = valor_motoboy(content['cep'])
            # Acessando os valores específicos
            servico_sedex = valores['servicos']['04162']
            servico_pac = valores['servicos']['04669']

            context = {
                'valormotoboy': valormotoboy,
                'tempopac': servico_pac['PrazoEntrega'],
                'temposedex': servico_sedex['PrazoEntrega'],
                'valorsedex': servico_sedex['Valor'],
                'valorpac': servico_pac['Valor'],
                'rua': content['logradouro'],
                'cidade': content['localidade'],
                'bairro': content['bairro'],
                'cep': content['cep'],
                'uf': content['uf']

            }

        else:
            context = {
                'erro': f'O cep: {cep} não foi encontrado na base de dados',
            }

        criar_cliente(request)
        return render(request, 'app_CotacaoEntregas/cotacao.html', context)
    else:
        return render(request, 'app_CotacaoEntregas/cotacao.html')


def criar_cliente(request):
    if request.method == "POST":
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
        
