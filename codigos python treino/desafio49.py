numero = int(input('Insira o numero que deseja ver a tabuada\n>>'))
n = int(input('Insira ate que numero deve ser multiplicado\n>>'))
i = 0
print('---INICIANDO A TABUADA----\n')
for i in range(n + 1):
    multiplicacao = numero * i
    print(f'{numero} X {i} = {multiplicacao}\n')
