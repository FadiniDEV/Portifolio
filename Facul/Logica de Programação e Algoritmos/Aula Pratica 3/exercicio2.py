print("\n\nCalculadora Simples\n\n" \
    "Digite a operação (+, -, *, /)\n" \
    "Ou pressione qualquer tecla para encerrar o programa\n")

op = input("")

if op not in ['+', '-', '*', '/']:
    print("\n\nPrograma encerrado.")

else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if op == '+':
        resultado = num1 + num2
        print(f"\n\nO resultado da adição é: {resultado:.2f}")

    elif op == '-':
        resultado = num1 - num2
        print(f"\n\nO resultado da subtração é: {resultado:.2f}")

    elif op == '*':
        resultado = num1 * num2
        print(f"\n\nO resultado da multiplicação é: {resultado:.2f}")

    elif op == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"\n\nO resultado da divisão é: {resultado:.2f}")
        else:
            print("\n\nErro: Divisão por zero não é permitida.")

    else:
        print("\n\nErro: Operação inválida.")