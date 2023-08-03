import requests
from decouple import config

key = config('KEY_CORREIO')
url = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={key}"

def valor_correio(cep):
    payload = {
    "cep_origem": "30170-130",
    "cep_destino": cep,
    "peso": 12,
    "comprimento": "25",
    "altura": "40",
    "largura": "11",
    "servicos": ["04162", "04669"]
}
    headers = {
    "Content-Type": "application/json"
}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    return(data)

print(valor_correio(34600190))