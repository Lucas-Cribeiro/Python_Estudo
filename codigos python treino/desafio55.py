menor_peso = 0
maior_peso = 0
pessoa_atual = 1
pessoa_mais_pesada = 0
peso_atual = float(input(f'Insira o peso da {pessoa_atual}°\n>>'))
menor_peso = peso_atual
pessoa_mais_leve = 1
for i in range(4):

    if peso_atual > maior_peso:
        maior_peso = peso_atual
        pessoa_mais_pesada = pessoa_atual
    if peso_atual < menor_peso:
        menor_peso = peso_atual
        pessoa_mais_leve = pessoa_atual
    pessoa_atual += 1
    peso_atual = float(input(f'Insira o peso da {pessoa_atual}°\n>>'))
    if peso_atual > maior_peso:
        maior_peso = peso_atual
        pessoa_mais_pesada = pessoa_atual
    if peso_atual < menor_peso:
        menor_peso = peso_atual
        pessoa_mais_leve = pessoa_atual


print(
    f'A pessoa mais pesada foi a {pessoa_mais_pesada}° pesando {maior_peso}kg.')
print(
    f'A pessoa mais leve foi a {pessoa_mais_leve}° pesando {menor_peso}kg.')
