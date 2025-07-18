import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from receber_cotacoes import converter_moeda

#Congfig janela principal
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x650")

dic_conversoes_disponiveis = conversoes_disponiveis()

#Elementos da Tela
titulo = customtkinter.CTkLabel(janela, text="TRADUTOR DE DINHEIRO", font=("ARIAL BLACK",20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Moeda de Origem:")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Moeda de Destino:")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma Moeda de Origem"])

# Função de validação para aceitar float
def validar_float(texto):
    if texto == "" or texto == "-":
        return True
    if texto.replace(",", "").replace(".", "").isdigit():
        return True
    return False

validacao = janela.register(validar_float)

# Criando o campo de entrada numérica
campo_quantidade = customtkinter.CTkEntry(janela, validate="key", validatecommand=(validacao, "%P"))

#Ação do programa
def converter():
    quantidade = campo_quantidade.get().replace(",", ".")
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()

    if moeda_origem and moeda_destino and quantidade:
        quantidade_float = float(quantidade)
        cotacao = converter_moeda(moeda_origem, moeda_destino)
        cotacao_float = float(cotacao)
        cotacao_final = quantidade_float * cotacao_float
        texto_cotacao_moeda.configure(text=f"Valor atualizado da cotação:\n{quantidade_float:.2f} {moeda_origem} = {cotacao_final:.2f} {moeda_destino}")

botao = customtkinter.CTkButton(janela, text="Converter", command=converter)

#Texto da cotação final (Sem config)
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

#Janela Scrolavel de Moedas
lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas = nomes_moedas()
for codigo_moeda in moedas:
    nome_moeda = moedas[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()


#Organização dos elementos da janela principal
titulo.pack(padx=10, pady=30)
texto_moeda_origem.pack(padx=10, pady=10)
campo_quantidade.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao.pack(padx=10, pady=35)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10)

#mainloop
janela.mainloop()