import forca
import adivinhacao

print("*********************************")
print("******\Selecione Seu Games/******")
print("*********************************")

print("\n(1) ENFORCADO (2) ADIVINHÃO\n")

jogo = int(input("Qual quieres?\n"))

if(jogo == 1):
    print("Bora pro ENFORCADO então")
    forca.jogar()
elif(jogo == 2):
    print("Bora pro ADIVINHÃO então")
    adivinhacao.jogar()
else:
    print("ESCOLHE UM DOS JOGOS EXISTENTES GARAIO")