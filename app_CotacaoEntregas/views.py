from django.shortcuts import render
from funcoes.cep import consultar_cep

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

            context = {
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


"""if cep == '':
    context = {'erro': 'Favor digitar um CEP para continuar'}
    return render(request, 'app_CotacaoEntregas/cotacao.html', context)

if content and not content.get('erro'):
    context = {
        'rua': content['logradouro'],
        'cidade': content['localidade'],
        'bairro': content['bairro'],
        'cep': content['cep'],
        'uf': content['uf']
    }
else:
    context = {
        'erro': f'O CEP {cep} não foi encontrado na base de dados',
    }

return render(request, 'app_CotacaoEntregas/cotacao.html', context)"""
