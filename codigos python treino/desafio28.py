import random
import time
numero_aleatorio = random.randint(0, 5)
numero_usuario = int(
    input('Insira um valor de 1 a 5 pra ver se você ta bem de adivinhação\n>>'))
print('Processando...')
time.sleep(2)
if numero_usuario == numero_aleatorio:
    print('QUE ISSO EM, TU ACERTOU. BOA MAE DINAH !!!!')
else:
    print('É tu não pode trabalhar de cartomante... TA ERRADO')
    print(
        f'\nO numero na verdade era: {numero_aleatorio}. Tenta de novo, colega ')
