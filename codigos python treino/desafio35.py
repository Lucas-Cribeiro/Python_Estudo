reta_1 = int(input('Insira o valor da primeira reta\n>>'))
reta_2 = int(input('Insira o valor da segunda reta\n>>'))
reta_3 = int(input('Insira o valor da terceira reta\n>>'))
if reta_1 + reta_2 > reta_3 and reta_2 + reta_3 > reta_1 and reta_1 + reta_3 > reta_2:
    print('É possivel formar um triângulo com os tamanhos das retas fornecidos')
else:
    print('Não é possivel formar um triângulo pois uma ou mais retas é maior que a soma das outras duas')
