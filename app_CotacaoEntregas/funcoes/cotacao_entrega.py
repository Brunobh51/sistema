import requests
from decouple import config

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'erro':'O CEP informado é inválido ou inexistente'}

def valor_correio(cep, peso):
    key = config('KEY_CORREIO')
    url = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={key}"
    payload = {
        "cep_origem": "30170-130",
        "cep_destino": cep,
        "peso": peso,
        "comprimento": "",
        "altura": "2",
        "largura": "12",
        "servicos": ["04162", "04669"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    return (data)

def valor_motoboy(cep):
    token_borzo = config('TOKEN_BORZO')
    url = 'https://robotapitest-br.borzodelivery.com/api/business/1.4/calculate-order'
    header = {
        'X-DV-Auth-Token': token_borzo,
        'Content-Type': 'application/json',
    }

    data = {
        "matter": "Documents",
        "points": [
            {
                "address": "30170-130"
            },
            {
                "address": cep
            }
        ]
    }
    response = requests.post(url, headers=header, json=data).json()
    valor_boy = int(float(response['order']['payment_amount']))

    if valor_boy <= 18:
        valor = '18,00'
        return valor
    else:
        return response['order']['payment_amount']
