numero_1 = int(input('Insira o primeiro numero\n>>'))
numero_2 = int(input('Insira o segundo numero\n>>'))
if numero_1 > numero_2:
    print(f'O valor {numero_1} é o maior ')
elif numero_2 > numero_1:
    print(f'O valor {numero_2} é o maior')
else:
    print('Os dois valores são iguais')
