import requests

def verificar_acessibilidade(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O site {url} está acessível.")
        else:
            print(f"O site {url} retornou o código de status {response.status_code}.")
    except requests.ConnectionError:
        print(f"Não foi possível conectar ao site {url}.")

# Exemplo de uso:
verificar_acessibilidade("https://www.pudim.com")
