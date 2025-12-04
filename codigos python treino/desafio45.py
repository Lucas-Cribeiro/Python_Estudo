import random
import time
jogar = 1
while jogar == 1:  
    jogador_1 = int(input('\nVamos jogar Jokenpo contra o computador. Escolha uma das opções para pedra, papel ou tesoura\n[1] Pedra\n[2] Papel\n[3]Tesoura\n>>'))
    computador = random.randint(1, 3)
    if jogador_1 > 3 or jogador_1 < 1:
        print('Escolha inválida. Escolha dentre as opções possiveis.')
        continue
    print('\nJO')
    time.sleep(0.8)
    print('Ken')
    time.sleep(0.8)
    print('PO')
    time.sleep(0.6)
    if jogador_1 == 1:
        escolha_jogador = 'Pedra' 
    elif jogador_1 == 2:
        escolha_jogador = 'Papel'
    elif jogador_1 == 3:
        escolha_jogador = 'Tesoura'

    if computador == 1:
        escolha = 'Pedra' 
    elif computador == 2:
        escolha = 'Papel'
    elif computador == 3:
        escolha = 'Tesoura'

    if((computador == 1 and jogador_1 == 3) or (computador == 2 and jogador_1 == 1) or (computador == 3 and jogador_1 == 2)):
        print (f'\nVocê perdeu! O computador escolheu {escolha} e você {escolha_jogador}.\nTente de novo.\n')
    elif(( jogador_1 == 1 and computador == 3) or ( jogador_1 == 2 and computador == 1) or (jogador_1 == 3 and computador == 2)):
        print (f'\nVocê venceu! O computador escolheu {escolha} e você {escolha_jogador}.\nPARABÉNS.\n')
    else:
        print(f'\nDeu empate! Ambos escolheram {escolha}\n')
    jogar = int(input('Deseja jogar novamente ?\n[1] Jogar de novo\n[2] Sair\n>>'))
    print
    if jogar == 2 :
        print('\nObrigado por jogar!')
        break

