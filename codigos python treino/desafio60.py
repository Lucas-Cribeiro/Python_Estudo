numero = int(input('Insira um número para achar o fatorial do mesmo.\n>>'))
atual = numero
fatorial = 1
while atual != 1:
    fatorial = fatorial * atual
    atual -=1

print(f'O fatorial de {numero} é = {fatorial}')