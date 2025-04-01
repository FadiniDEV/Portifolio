import customtkinter

#Congfig janela principal
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

#Elementos da Tela
titulo = customtkinter.CTkLabel(janela, text="TRADUTOR DE DINHEIRO", font=("ARIAL BLACK",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])

#Ação do programa
def converter ():
    print("Convertido")

botao = customtkinter.CTkButton(janela, text="Converter", command=converter)

#Janela Scrolavel de Moedas
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas = ["USD: Dólar Americano", "BRL: Real Brasileiro", "EUR: Euro", "BTC: Bitcoin"]
for moeda in moedas:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
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