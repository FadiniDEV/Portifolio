print("\n\nBem vindo ao plano de saúde do Lucas Fadini Apolinário!\n\n")

# Laço para permitir que o usuário faça várias simulações de cálculo do valor do plano de saúde
while True:
    valorBase = input("Digite o valor base do plano de saúde: ")
    idade = input("\nDigite a idade do cliente: ")

    # verifica se a idade e o valor base são numeros removendo qualquer string ou booleano que o 
    # usuário possa ter digitado arrumando o crash caso o usuario digitasse uma string em algum valor
    if idade.isdigit() and valorBase.replace('.', '').isdigit():
        idade = int(idade)
        valorBase = float(valorBase)

        # Calcula o valor mensal do plano de saúde com base na idade do cliente
        if idade >= 0 and idade < 19:
            valorMensal = valorBase * (100 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")
        elif idade >= 19 and idade < 29:
            valorMensal = valorBase * (150 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")
        elif idade >= 29 and idade < 39:
            valorMensal = valorBase * (225 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")
        elif idade >= 39 and idade < 49:
            valorMensal = valorBase * (240 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")
        elif idade >= 49 and idade < 59:
            valorMensal = valorBase * (350 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")
        else:
            valorMensal = valorBase * (600 / 100)
            print(f"\n\nO valor do plano de saúde para o cliente informado é de: R${valorMensal:.2f}")

    else:
        print("\n\nIdade ou Valor base do Plano inválida. Por favor, insira apenas valores númericos.\n")
        continue

    # Pergunta ao usuário se deseja calcular o valor do plano de saúde para outro cliente
    continuar = input("\n\nDeseja calcular o valor do plano de saúde para outro cliente? (S/N) ")

    if continuar.upper() == 'S':
        print("\nEntão vamos fazer uma nova simulação!\n\n")
    elif continuar.upper() == 'N':
        print("\nObrigado por usar o plano de saúde do Lucas Fadini Apolinário!\n\n")
        break
    else:
        print("\nOpção inválida. Encerrando o programa...\n\n")
        break

