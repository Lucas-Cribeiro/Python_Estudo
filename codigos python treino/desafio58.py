import random
import time
numero_aleatorio = random.randint(0, 10)
numero_usuario = int(
    input('Insira um valor de 1 a 10 pra ver se você ta bem de adivinhação\n>>'))
print('Processando...')
time.sleep(2)
tentativa = 1
while numero_usuario != numero_aleatorio:
    print('É tu não pode trabalhar de cartomante... TA ERRADO')
    numero_usuario = int(input(
        f'\nTenta de novo, colega\n>> '))
    tentativa += 1
    print('Processando...')
    time.sleep(2)
if numero_usuario == numero_aleatorio and tentativa == 1:
    print('QUE ISSO EM, TU ACERTOU DE PRIMEIRA. BOA MAE DINAH !!!!')
elif numero_aleatorio == numero_usuario and (tentativa > 1 and tentativa < 5):
    print(f'Acertou, pae. BOA. Você precisou tentar {tentativa} vezes.')
else: 
    print(f'Tava dificil ai em... Tu levou {tentativa} tentativas pra acertar, melhore... Mas boa.')


