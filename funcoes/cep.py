import requests


def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

"""def con_valor_correio_para_cep(cep, peso):
    dados_cep = consultar_cep(cep)
    if dados_cep:
        valor_frete = con_valor_correio(dados_cep, peso)  # Correção aqui
        return valor_frete
    else:
        return None

# Exemplo de uso
cep = '12345-678'
peso = 1.5
valor_frete = con_valor_correio_para_cep(cep, peso)

if valor_frete:
    print(f"Valor do frete para o CEP {cep}: {valor_frete}")
else:
    print("Não foi possível calcular o frete.")
"""
"""# Exemplo de uso
cep = '12345-678'
peso = 1.5
valor_frete = con_valor_correio_para_cep(cep, peso)

if valor_frete:
    print(f"Valor do frete para o CEP {cep}: {valor_frete}")
else:
    print("Não foi possível calcular o frete.")"""
