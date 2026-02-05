print("\n\nBem vindo ao sistema que calcula o valor a ser pago pelo aluguel de um carro!\n\n")

cliente = input("Por favor, digite o nome do cliente: ")
km = float(input("Digite a distância em km que foi percorrido: "))
dia = int(input("Digite a quantidade de dias que o carro foi alugado: "))

total_pagamento = 60 * dia + 0.15 * km

print(f"\n\nO total a ser pago pelo aluguel do carro de {cliente} é: R$ {total_pagamento:.2f}\n\n")
