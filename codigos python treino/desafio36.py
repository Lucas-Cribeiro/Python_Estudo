valor_casa = float(input(
    'Insira o valor total da casa para analisarmos um possivel emprestimo\n>>'))
salario = float(input('Insira o salario bruto do comprador\n>>'))
anos = int(input('Insira em quantos anos vai ser pago este emprestimo\n>>'))
prestacao = valor_casa / (anos * 12)
if prestacao > salario * 0.30:
    print(
        f'Empréstimo negado! O valor das prestações será {prestacao:.2f} e é maior que 30%" do salario do comprador')
else:
    print(
        f'Emprestimo aceito! O valor das prestações ficou de R${prestacao:.2f} por mês para pagar em {anos * 12} meses')
numero = int(input('Insira um numero inteiro para conversão:\n>>'))
escolha = int(input(
    'Escolha a conversão que deseja fazer: \n1 - binário\n2 - octal\n3 - hexadecimal\n>>'))
resto = 0
if escolha == 1:
    binario = bin(numero)
    print(f'Conversão binario = {binario}')
elif escolha == 2:
    octal = oct(numero)
    print(f'Conversão octal ={octal}')
elif escolha == 3:
    hexa = hex(numero)
    print(f'Conversão hexadecimal = {hexa}')
