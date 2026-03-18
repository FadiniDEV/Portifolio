def escolha_tipo():
    #laço para escolher o tipo de madeira que o cliente deseja comprar
    while True:

        print("\nEscolha o tipo de madeira que deseja comprar:")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia\n")

        madeira = input("Digite o código da madeira desejada: ")

        #if com base no input do cliente, independente se ele digitar minusculo ou maiusculo
        if madeira.upper() == "PIN" or madeira.upper() == "PINHO":
            valor = 150.40
            return valor

        elif madeira.upper() == "PER" or madeira.upper() == "PEROBA":
            valor = 170.20
            return valor

        elif madeira.upper() == "MOG" or madeira.upper() == "MOGNO":
            valor = 190.90
            return valor

        elif madeira.upper() == "IPE" or madeira.upper() == "IPE":
            valor = 210.10
            return valor

        elif madeira.upper() == "IMB" or madeira.upper() == "IMBUIA":
            valor = 220.70
            return valor

        else:
            print("\nCódigo de madeira inválido. Por favor, insira um código válido.\n")
            continue
        

def qtd_toras():
    #Laço para definir a quantidade de toras e resetar caso o cliente digite algo errado
    while True:
        #try para verificar se o cliente digitou apenas valores inteiros
        try:
            quantidade = int(input("Digite a quantidade de toras que deseja comprar: "))
            
            #if para devolver para o programa principal a quantidade que o cliente deseja e o desconto em formato de lista

            if quantidade < 0: #Removendo a possibilidade de numeros negativos
                print("\nQuantidade inválida. Por favor, insira um número positivo.\n")
                continue

            elif quantidade < 100:
                desconto = 0
                qtd_desconto = [quantidade, desconto]
                return qtd_desconto
            
            elif quantidade >= 100 and quantidade < 500:
                desconto = 4 / 100
                qtd_desconto = [quantidade, desconto]
                return qtd_desconto
            
            elif quantidade >= 500 and quantidade < 1000:
                desconto = 9 / 100
                qtd_desconto = [quantidade, desconto]
                return qtd_desconto
            
            elif quantidade >= 1000 and quantidade <= 2000:
                desconto = 16 / 100
                qtd_desconto = [quantidade, desconto]
                return qtd_desconto
            
            else:
                print("\nNão são aceitos pedidos com essa quantidade de toras!\nPor favor, entre novamente com a quantidade.\n")
                continue

        #Erro caso o cliente digite um valor que não seja inteiro
        except ValueError:
            print("\nEntrada inválida. Por favor, insira um número inteiro.\n")
            continue
        

def transporte():

    #Laço para escolher o tipo de transporte ou voltar caso tiver algum erro
    while True:
        print("\nEscolha o tipo de transporte desejado:")
        print("1 - Transporte Rodoviário - R$ 1000,00")
        print("2 - Transporte Ferroviário - R$ 2000,00")
        print("3 - Transporte Hidroviário - R$ 2500,00\n")

        #Try para filtrar valores inteiros
        try:
            transporte = int(input("Digite o tipo de transporte desejado: "))

            if transporte == 1:
                valor_transporte = 1000.00
                return valor_transporte

            elif transporte == 2:
                valor_transporte = 2000.00
                return valor_transporte

            elif transporte == 3:
                valor_transporte = 2500.00
                return valor_transporte

            #Filtro para que o cliente digite apenas os numeros 1, 2 e 3
            else:
                print("\nTipo de transporte inválido. Por favor, insira um tipo válido.\n")
                continue

        except ValueError:
            print("\nEntrada inválida. Por favor, insira apenas uma das opções.\n")
            continue

print("Bem vindo a madeireira do Lucas Fadini Apolinário!")

while True:
    valor_madeira = escolha_tipo()
    qtd_desconto = qtd_toras()
    adicional_transporte = transporte()
    
    #Formula para calcular o valor total da cotação
    total = ((valor_madeira * qtd_desconto[0])*(1 - qtd_desconto[1])) + adicional_transporte

    print(f"\nO valor total da compra é de: R${total:.2f}\n")

    #Continuidade do laço para não ter que iniciar o programa novamente caso o cliente queira uma nova cotação
    continuar = input("Deseja fazer uma nova simulação? (S/N) ")

    if continuar.upper() == "S":
        print("\nEntão vamos para uma nova simulação!\n\n")
        continue
    else:
        print("\nObrigado por usar a madeireira do Lucas Fadini Apolinário!\n\n")
        break