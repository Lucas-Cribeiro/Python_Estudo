dinheirobr = float(
    input('Insira a quantidade de dinheiro que você tem em R$\n>>'))
dolar = dinheirobr/5.38
print('É possivel pegar ${:.2f} dolares com R${:.2f} que você tem na carteira'.format(
    dolar, dinheirobr))
