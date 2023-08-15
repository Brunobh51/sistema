from django.shortcuts import render
from .funcoes.cotacao_entrega import consultar_cep, valor_correio, valor_motoboy
from .models import Cliente
from .forms import FormularioCadastro, FormularioEndereco

# Constantes
SERVICO_SEDEX = '04162'
SERVICO_PAC = '04669'


def dashboard(request):
    return render(request, 'dashboard.html')


def cotacao(request):
    if request.method == "POST":
        cep = request.POST.get('cep')
        content = consultar_cep(cep)
        form = FormularioCadastro
        formEndereco = FormularioEndereco

        if not cep:
            context = {'erro': 'Favor digitar um CEP para continuar'}
            return render(request, 'app_CotacaoEntregas/cotacao.html', context)

        if content and not content.get('erro'):
            peso = request.POST.get('peso')
            valores = valor_correio(content['cep'], peso)
            valormotoboy = valor_motoboy(content['cep'])

            servico_sedex = valores['servicos'][SERVICO_SEDEX]
            servico_pac = valores['servicos'][SERVICO_PAC]

            initial_data = {
                'cep': cep,
                'rua': content['logradouro'],
                'bairro': content['bairro'],
                'cidade': content['localidade'],
                'estado': content['uf']

            }
            initial_data_valor = {
                'valor_boy': valormotoboy
            }

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
                'uf': content['uf'],
                'form': form(initial=initial_data_valor),
                'formEndereco': formEndereco(initial=initial_data)
            }
        else:
            context = {
                'erro': f'O CEP {cep} não foi encontrado na base de dados'}

        return render(request, 'app_CotacaoEntregas/cotacao.html', context)
    else:
        return render(request, 'app_CotacaoEntregas/cotacao.html')


def lista_entregas(request):
    if request.method == "POST":
        nome = request.POST.get('nome_cliente')
        print(nome)

    return render(request, 'app_CotacaoEntregas/criacao_entrega.html')


def formulario(request):
    form = FormularioCadastro()
    return render(request, 'app_CotacaoEntregas/home.html', {'form': form})
