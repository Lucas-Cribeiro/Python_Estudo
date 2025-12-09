media = 0
total_idade = 0
mulheres_menos_20 = 0
pessoa = 0
mais_velho = 0
nome_mais_velho = ''
for i in range(4):
    pessoa += 1
    nome_atual = input(f'Insira o nome da {pessoa}° pessoa\n>>')
    idade_atual = int(input(f'Insira a idade da {pessoa}° pessoa\n>>'))
    sexo_atual = input(
        f'Insira "F"" para sexo feminino ou "M" para sexo masculino da {pessoa}° pessoa\n>>')
    if (idade_atual > mais_velho) and (sexo_atual == 'M' or sexo_atual == 'm'):
        nome_mais_velho = nome_atual
        mais_velho = idade_atual
    if sexo_atual == 'F' or sexo_atual == 'f':
        if idade_atual < 20:
            mulheres_menos_20 += 1
    total_idade += idade_atual

media = total_idade / pessoa
print(f'A média de idade dentre {pessoa} pessoas, ficou = {media:.2f}')
if mais_velho > 0:
    print(f'O nome do homem mais velho é {nome_mais_velho}')
else:
    print('Nenhum homem foi cadastrado.')
print(f'A quantidade de mulheres com menos de 20 anos = {mulheres_menos_20}')
