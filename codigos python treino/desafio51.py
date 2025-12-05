primeiro_termo = int(input('Insira o primeiro termo da PA.\n>>'))
razao = int(input('Insira a razão desta PA.\n>>'))
termo = 1
pa = primeiro_termo
for i in range(10):
    print(f'Termo a{termo} = {pa}')
    pa = pa + razao
    termo += 1
