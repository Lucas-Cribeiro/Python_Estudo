velocidade = float(
    input('Qual foi a velocidade que o carro passou no radar ?\n>>'))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7
    print(
        f'Você foi multado, sua velocidade estava de {velocidade}km/h. O maximo permitido na via é de 80km/h. Dirija-se ao site do detran para pagar sua multa de valor R$ {multa:.2f}')
else:
    print(
        f'Sem multa, sua velocidade foi {velocidade}km/h, siga em paz e com cautela')
