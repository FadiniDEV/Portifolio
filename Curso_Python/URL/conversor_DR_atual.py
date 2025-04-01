import requests
from extratorurl import ExtratorURL

def get_valor_dolar():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["rates"].get("BRL", None)  # Obtém a cotação USD -> BRL
    else:
        return None

def opcao_real():
    valor = input("\nSelecione o valor em Reais: ")
    valor = float(valor.replace('.','').replace(',','.').replace(" ", ""))
    convertido = valor / get_valor_dolar()
    print(f"R${valor:.2f} convertido em dolar é ${convertido:.2f}\n")

def opcao_dolar():
    valor = input("\nSelecione o valor em Dolar: ")
    valor = float(valor.replace('.','').replace(',','.').replace(" ", ""))
    convertido = valor * get_valor_dolar()
    print(f"${valor:.2f} Dolares convertido em Reais é R${convertido:.2f}\n")

def info_url():
    url = input("\nInsira a URL da BYTEBANK:\n")
    extrator_url = ExtratorURL(url)
    print("\n\nO tamanho da URL é: ", extrator_url.__len__(url))
    print("URL completa: ", extrator_url.__str__(url))
    valor_quantidade = extrator_url.get_valor_parametro("quantidade")
    print("Valor do parâmetro 'quantidade': ", valor_quantidade, "\n")

def converte_url():
    url = input("\nDigite a URL do BYTEBANK:\n")
    extrator_url = ExtratorURL(url)
    moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
    moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
    quantidade = extrator_url.get_valor_parametro("quantidade")
    quantidade = float(quantidade.replace('.','').replace(',','.').replace(" ", ""))

    if moeda_origem == "real" and moeda_destino == "dolar":
        valor_conversao = int(quantidade) / get_valor_dolar()
        print(f"\nO valor de R${quantidade:.2f} reais é igual a ${valor_conversao:.2f} dólares.\n")
    elif moeda_origem == "dolar" and moeda_destino == "real":
        valor_conversao = int(quantidade) * get_valor_dolar()
        print(f"\nO valor de ${quantidade:.2f} dólares é igual a R${valor_conversao:.2f} reais.\n")
    else:
        print(f"\nCâmbio de {moeda_origem} para {moeda_destino} não está disponível.\n")

def fechar_programa():
    print("\nFechando Programa...\n")
    exit()

def erro():
    print("\nSelecione Uma das Opções Abaixo!\n")


laco = 0
while(laco == 0):
    moeda = input("\nO que pretende fazer?\n(1)Converter Real para Dolar (2)Converter Dolar para Real (3)URL Infos (4)Converter pela URL (x)Fechar Programa\n\nDigite uma Opção: ")

    if moeda == "1":
        opcao_real()

    elif moeda == "2":
        opcao_dolar()

    elif moeda == "3":
        info_url()

    elif moeda == "4":
        converte_url()
    
    elif moeda == "x":
        fechar_programa()

    else:
        erro()