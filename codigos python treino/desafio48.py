soma = 0
i = 0
while i < 501:
    if i % 3 == 0 and i % 2 != 0:
        valor = i
        soma += valor
    i += 1

print(f'A soma de todos os numeros multiplos de 3 é = {soma}')
