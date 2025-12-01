distancia = float(input('Insira a distância da sua viagem em km\n>> '))
valor = 0
if distancia <= 200:
    valor = 0.50 * distancia
else:
    valor = 0.45 * distancia

print(f'O valor a pagar da sua viagem é de R${valor:.2f}')
