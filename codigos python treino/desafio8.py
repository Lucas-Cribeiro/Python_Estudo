metros = float(input('Insira o valor em metros\n>>'))
cm = metros * 100
mm = metros * 1000
print('O valor de {} metros em centímetros é {:.2f}'.format(metros, cm), end=' ')
print(f'e em milímetros é {mm}')
