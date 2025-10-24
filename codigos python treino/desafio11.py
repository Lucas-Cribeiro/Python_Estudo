largura = float(input('Insira a largura da parede em metros\n>>'))
altura = float(input('Insira a altura da mesma parede em metros\n>>'))
area = largura * altura
tinta = area / 2
print('A area da sua parede é = {:.1f}m e'.format(area), end=' ')
print(
    'a quantidade de tinta em litros necessaria para pinta-la é = {:.1f}l '.format(tinta))
