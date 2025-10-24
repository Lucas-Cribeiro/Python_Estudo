valor = float(input('Insira o valor do produto\n>>'))
desconto = valor * 0.05
novovalor = valor - desconto
print('O produto de valor :R${:.2f} após o desconto de 5%'.format(valor), end=' ')
print('fica com o novo preço de :R${:.2f}'.format(novovalor))
