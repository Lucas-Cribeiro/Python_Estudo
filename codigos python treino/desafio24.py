cidade = input('Insira o nome da cidade\n>>')
cidade_santo = cidade[:5]
if 'Santo' in cidade_santo:
    print(True)
else:
    print(False)

print(cidade)
print(cidade_santo)