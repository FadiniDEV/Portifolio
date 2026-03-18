print("Escolha o que deseja comprar: ")
print("1 - Arroz")
print("2 - Feijão")
print("3 - Macarrão")

produto = int(input("Digite o número do produto: "))
qtde = int(input("Digite a quantidade: "))

match (produto):
    case 1:
        print(f"Você comprou {qtde} kg de arroz, totalizando R${qtde * 5:.2f}")
    case 2:
        print(f"Você comprou {qtde} kg de feijão, totalizando R${qtde * 7.50:.2f}")
    case 3:
        print(f"Você comprou {qtde} kg de macarrão, totalizando R${qtde * 4:.2f}")
    case _:
        print("Produto inválido.")