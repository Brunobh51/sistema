import requests

def consultar_cep(cep):
    cep = cep 
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url).json()
    dec_response = dict(response)
    return dec_response





