from django.shortcuts import render
from funcoes.cep import consultar_cep
from funcoes.correio import valor_correio
from funcoes.motoboy_borzo import valor_motoboy
"""
# Acessando os valores específicos
servico_sedex = response['servicos']['04162']
servico_pac = response['servicos']['04669']

"""

def dashboard(request):
    return render(request, 'dashboard.html')

def cotacao(request):
    if request.method == "POST":
        cep = request.POST.get('cep')
        content = consultar_cep(cep)
        if cep == '':
            context={'erro': 'Favor digitar um cep para continuar' }
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
        
        return render(request, 'app_CotacaoEntregas/cotacao.html', context)
    else:
        return render(request, 'app_CotacaoEntregas/cotacao.html')
