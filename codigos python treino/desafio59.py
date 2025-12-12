valor_a = int(input('Insira o seu primeiro valor\n>>'))
valor_b = int(input('Insira o seu segundo valor\n>>'))
opcao = 0
while opcao != 5:
    opcao = int(input(
        '\nEscolha a operação que deseja fazer ou a ação dentro deste programa de dois valores\n[1]Somar\n[2]Multiplicar\n[3]Maior Número\n[4]Novos números\n[5]Sair\n>>'))
    if opcao == 1:
        soma = valor_a + valor_b
        print(f'A soma entre {valor_a} e {valor_b} = {soma}')
    elif opcao == 2:
        multi = valor_a * valor_b
        print(f'A multiplicação entre {valor_a} e {valor_b} = {multi}')
    elif opcao == 3:
        maior = valor_a
        if valor_a == valor_b:
            print('Os dois valores são iguais, não há maior.')
        else:
            if valor_b > valor_a:
                maior = valor_b
            print(f'O maior valor é o {maior}')
    elif opcao == 4:
        valor_a = int(input('Insira um novo valor pro primeiro número\n>>'))
        valor_b = int(input('Insira um novo valor para o segundo número\n>>'))
    elif opcao > 5 or opcao < 1:
        print('Opção inválida, selecione uma opção dentre as demonstradas no menu.')
print('Saindo do programa...')
