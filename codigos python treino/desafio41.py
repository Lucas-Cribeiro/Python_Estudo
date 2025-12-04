from datetime import date
ano = int(input('Insira o ano de nascimento do atleta\n>>'))
ano_atual = date.today().year
if ano > ano_atual:
    print('ANO INVALIDO.\nAno de nascimento não pode ser maior que o ano atual.')
else:
    idade = ano_atual - ano
    if idade <= 9:
        print(f'IDADE:{idade}\nCATEGORIA: MIRIM')
    elif idade > 9 and idade <= 14:
        print(f'IDADE: {idade}\nCATEGORIA: INFANTIL')
    elif idade > 14 and idade <= 19:
        print(f'IDADE: {idade}\nCATEGORIA: JUNIOR')
    elif idade <= 25:
        print(f'IDADE: {idade}\nCATEGORIA: SENIOR')
    else:
        print(f'IDADE: {idade}\nCATEGORIA: MASTER')
