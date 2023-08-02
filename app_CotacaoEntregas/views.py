from django.shortcuts import render
from funcoes.cep import consultar_cep

def dashboard(request):
    return render(request, 'dashboard.html')

def cotacao(request):
    if request.method == "POST":
        cep = request.POST.get('cep', '')
        context = consultar_cep(cep)
        context = {'rua': context['logradouro'],
                    'cidade': context['localidade'],
                    'bairro': context['bairro'],
                    'cep': context['cep'],
                    'uf': context['uf']}
        
        


        return render(request, 'app_CotacaoEntregas/cotacao.html', context)
    else:
        return render(request, 'app_CotacaoEntregas/cotacao.html')
