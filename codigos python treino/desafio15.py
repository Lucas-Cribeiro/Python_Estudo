kmrodados = float(input('Insira os quilometros rodados pelo veículo\n>>'))
dias = int(input('Insira a quantidade de dias que este carro ficou alugado\n>>'))
valordias = dias * 60
valorkm = kmrodados * 0.15
valortotal = valorkm + valordias
print('O valor total a se pagar pelo carro é = R${:.2f}'.format(valortotal))
