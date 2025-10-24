salario = float(input('Insira o salario do funcionario\n>>'))
aumento = salario * 0.15
novosalario = salario + aumento
print('O salario do funcionario era: R${:.2f}'.format(salario), end=' ')
print('e após o aumento de 15%, o salario atual ficou de R${:.2f}'.format(
    novosalario))
