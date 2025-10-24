#Codigo para randomizar o tempo de envio das campanhas
import time
import random
x = int(input('Insira um valor\n>>'))
y = x + 4
tempo_de_pausa = random.randint(1800, 2200)
print('O programa irá parar por {:.2f} minutos'.format(tempo_de_pausa / 60))
time.sleep(tempo_de_pausa)
print('Pausa finalizada')
print('Y é igual a {}'.format(y))
input('Pressione enter para sair...')
