numero = int(input('Insira um numero para verificar se ele é primo\n>>'))
divisor = 1
primo = 0
for i in range(numero):
    if numero % divisor == 0:
        primo += 1
    divisor+= 1
if primo == 2:
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')