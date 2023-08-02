import requests
from decouple import config

key = config('KEY_CORREIO')

url = f"https://www.sgpweb.com.br/novo/api/consulta-precos-prazos?chave_integracao={key}"

payload = {
    "cep_origem": "30170-130",
    "cep_destino": "32113-290",
    "peso": "3,75",
    "comprimento": "25",
    "altura": "40",
    "largura": "11",
    "servicos": ["04162", "04669"]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers).json()

# Acessando os valores específicos
servico_04162 = response['servicos']['04162']
servico_04669 = response['servicos']['04669']

print("Serviço 04162:")
print(f"Valor: {servico_04162['Valor']}")
print(f"Prazo de Entrega: {servico_04162['PrazoEntrega']} dias\n")

print("Serviço 04669:")
print(f"Valor: {servico_04669['Valor']}")
print(f"Prazo de Entrega: {servico_04669['PrazoEntrega']} dias")
