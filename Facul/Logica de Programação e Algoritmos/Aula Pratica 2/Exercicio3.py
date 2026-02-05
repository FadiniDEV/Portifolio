print("\n\nBem vindo ao programinha que exibe a metade de uma frase!\n\n")

frase = input("Digite uma frase: ")
tamanho = len(frase)
metade = frase[:tamanho // 2]

print(f"\n\nOs 2 ultimos caracteres da metade são: {metade[-2:]}\n\n")

