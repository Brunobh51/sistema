from django.shortcuts import render
from funcoes.cep import consultar_cep

def dashboard(request):
    return render(request, 'dashboard.html')

def cotacao(request):
    if request.method == "POST":
        cep = request.POST.get('cep', '')
        context = consultar_cep(cep)
        contexto = {'cep': context['logradouro']}
        return render(request, 'app_CotacaoEntregas/cotacao.html', contexto)
    else:
        return render(request, 'app_CotacaoEntregas/cotacao.html')
