salario = float(input('Insira o salário do funcionario\n>>'))
aumento = 0.0
if salario > 1250.00:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15
salario_novo = salario + aumento
print(
    f'O salário do funcionario com aumento de R${aumento:.2f} ficou igual a: R${salario_novo:.2f}')
