import requests
from decouple import config

token_borzo = config('TOKEN_BORZO')
url = 'https://robotapitest-br.borzodelivery.com/api/business/1.4/calculate-order'


def valor_motoboy(cep):
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
