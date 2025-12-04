valor_produto = float(input('Insira o valor do produto\n>> R$'))
forma_pagamento = int(
    input('Qual será a forma de pagamento ?\n1 - Dinheiro/Cheque\n2 - Cartão\n>>'))
if forma_pagamento == 1:
    desconto = valor_produto * 0.10
    valor_final = valor_produto - desconto
elif forma_pagamento == 2:
    cartao = int(input('Pagamento no cartão a vista ?\n1 - Sim\n2 - Não\n>>'))
    if cartao == 1:
        desconto = valor_produto * 0.05
        valor_final = valor_produto - desconto
    elif cartao == 2:
        vezes = int(input('Quantas vezes irá dividir ? \n>> '))
        if vezes == 2:
            valor_final = valor_produto
        elif vezes > 2:
            juros = valor_produto * 0.20
            valor_final = valor_produto + juros
print(f'O valor a pagar ficou = R${valor_final}')
