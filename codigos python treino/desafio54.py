pessoa = 1
menor_idade = 0
maior_idade = 0
for i in range(7):
    idade = int(input(f'Insira a idade da {pessoa}° pessoa\n>>'))
    if idade < 21:
        menor_idade += 1
    else:
        maior_idade += 1
    pessoa += 1
print(
    f'\nPessoas com maioridade : {maior_idade}\nPessoas menores de idade: {menor_idade}')
