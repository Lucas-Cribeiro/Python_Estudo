from datetime import date
ano = int(input('Insira o ano de nascimento\n>>'))
ano_atual = date.today().year
idade = ano_atual - ano
if idade == 18:
    print('Você esta no ano certo para se alistar. Procure o quartel mais proximo e siga as instruções. BOA SORTE!')
elif idade < 18:
    print(
        f'Você ainda não tem a idade correta para se alistar. Faltam {18 - idade} anos para você se alistar')
else:
    print(
        f'Você passou do prazo pra alistar. Você esta {idade - 18} anos atrasado. Procure oque deve ser feito para estar de acordo com o serviço militar obrigatorio.')
