print("Bem vindo ao meu programinha de testes!\n\n")

som_int = (10 + 15 + 11 + 70 + 2)
media = (23 + 19 + 31) / 3
divisao = (403 // 73)
sobra = 403 % 73
elevado = 2 ** 10
val_abs = abs(54 - 57)
minimo = min(34, 29, 31)

print(f"A soma dos números 10 + 15 + 11 + 70 + 2 é: {som_int}\n")
print(f"A média dos números 23 + 19 + 31 é: {media:.2f}\n")
print(f"O número 73 cabe *{divisao}* vezes no número 403\ncom sobra de: {sobra}\n")
print(f"O número 2 elevado a 10ª potencia é: {elevado}\n")
print(f"O valor absoluto da diferença entre 54 e 57 é: {val_abs}\n")
print(f"O menor valor entre 34, 29 e 31 é: {minimo}\n\n")


a = 3
b = 4
c = a * a + b * b

print(f"O valor de c na expressão c = a² + b²\nonde a = 3 e b = 4 é: {c}\n\n")


s1 = "ant"
s2 = "bat"
s3 = "cod"

print(s1 + " " + s2 + " " + s3)
print((s1 + " ") * 10)
print(s1 + " " + (s2 + " ") * 2 + (s3 + " ") * 3)
print((s1 + " " + s2 + " ") * 7)
print((s2 + s2 + s3 + " ") * 5 + "\n\n")