V1 = float(input("Digite o valor de V1: "))
V2 = float(input("Digite o valor de V2: "))
V3 = float(input("Digite o valor de V3: "))

if (V1 > 0 and V2 > 0 and V3 > 0) and (V1 + V2 > V3 and V1 + V3 > V2 and V2 + V3 > V1):
    if V1 == V2 == V3:
        print("Triângulo equilátero.")
    elif V1 != V2 and V1 != V3 and V2 != V3:
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("Triangulo invalido.")