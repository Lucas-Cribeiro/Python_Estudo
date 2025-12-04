peso = float(input('Insira o seu peso em kg\n>>'))
altura = float(input('Insira sua altura em metros\n>>'))
imc = peso / (altura * altura)
print(f'Seu IMC ficou = {imc:.2f}')
if imc < 18.5:
    print('Você esta abaixo do peso ideal para sua saúde.')
elif imc >= 18.5 and imc < 25:
    print('Você esta no peso ideal. Parabéns, continue assim.')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso. Tome cuidado para não engordar mais.')
elif imc >= 30 and imc < 40:
    print('Você esta com obesidade. Busque ajuda medica para não agravar seu caso.')
else:
    print('Você esta com obesidade morbida! Busque ajuda medica imediatamente e um tratamento o quanto antes.')
