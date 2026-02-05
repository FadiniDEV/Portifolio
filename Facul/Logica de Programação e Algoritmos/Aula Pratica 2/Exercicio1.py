nome = input("Seja bem vindo!\nPara começar, digite seu nome: ")

print(f"\n\nOlá, {nome}! Que bom ter você aqui!\
      \n\nEsse é um programinha simples para aplicar um percentual de desconto em um produto.\n\n")

preco_produto = float(input("Digite o preço do produto (apenas números): R$ "))
percentual_desconto = float(input("Digite a porcentagem de desconto (apenas números): "))
valor_desconto = (percentual_desconto / 100) * preco_produto
preco_final = preco_produto - valor_desconto

print(f"\n\nO preço original do produto é: R$ {preco_produto:.2f}\n\
        O valor do desconto é: R$ {valor_desconto:.2f}\n\
        O preço final do produto com desconto de {percentual_desconto}% é: R$ {preco_final:.2f}\n\n\
        Obrigado por usar meu programinha, {nome}!\n\n\
        Volte sempre!\n\n")