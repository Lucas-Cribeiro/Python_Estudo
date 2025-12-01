num1 = int(input('Insira o seu primeiro valor\n>>'))
num2 = int(input('Insira o seu segundo valor\n>>'))
num3 = int(input('Insira o seu terceiro valor\n>>'))
if (num1 > num2 and num1 > num3):
    print(f'O seu primeiro numero, {num1} é o maior dos três')
elif num2 > num1 and num2 > num3:
    print(f'O seu segundo numero, {num2} é o maior dos três')
else:
    print(f'O seu terceiro numero, {num3} é o maior dos três')
