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
            print(f'Sua compra ficou divida em 2 parcelas de R${valor_final / 2:.2f}')
        elif vezes > 2:
            juros = valor_produto * 0.20
            valor_final = valor_produto + juros
            print(f'Sua compra ficou divida em {vezes} parcelas de R${valor_final / vezes:.2f}')
print(f'O valor total a pagar ficou = R${valor_final:.2f}')
