numero = int(input('Insira o numero que deseja converter\n>>'))
escolha = int(input('Escolha qual conversão será feita.\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n>>'))
if escolha < 1 or escolha > 3:
    print('Escolha inválida, fechando programa...')
else:
    if escolha == 1:
        tipo = 'Binário'
        convertido = bin(numero)
    elif escolha == 2:
        tipo = 'Octal'
        convertido = oct(numero)
    elif escolha == 3:
        tipo = 'Hexadecimal'
        convertido = hex(numero)
    print(f'O seu númmero ({numero}) convertido em {tipo} ficou = {convertido}')
