import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis

#Congfig janela principal
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

#Elementos da Tela
titulo = customtkinter.CTkLabel(janela, text="TRADUTOR DE DINHEIRO", font=("ARIAL BLACK",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma Moeda de Origem"])

#Ação do programa
def converter ():
    print("Convertido")

botao = customtkinter.CTkButton(janela, text="Converter", command=converter)

#Janela Scrolavel de Moedas
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas = nomes_moedas()
for codigo_moeda in moedas:
    nome_moeda = moedas[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()


#Pad dos elementos da janela principal
titulo.pack(padx=10, pady=30)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao.pack(padx=10, pady=50)
lista_moedas.pack(padx=10)

#mainloop
janela.mainloop()