soma = 0
for i in range(6):
    numero = int(input('Insira um numero inteiro para somar. Saiba que so somaremos numeros pares.\n>>'))
    if numero % 2 == 0:
        soma += numero
print(f'Sua soma de pares ficou = {soma}')
