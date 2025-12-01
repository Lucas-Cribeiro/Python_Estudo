import json
import collections
import time
import random
# Quantidade de contatos que serão processados por disparo
TAMANHO_DO_DISPARO = 13
# Tempo de pausa entre cada disparo sendo de 30 a 60 minutos
PAUSA_MINIMA_DISPARO = 1800
PAUSA_MAXIMA_DISPARO = 3600
# Tempo de pausa para enviar o restante da fila
PAUSA_MINIMA_FILA = 300
PAUSA_MAXIMA_FILA = 600


def enviar_disparo_chamados(chamado_id: int) -> bool:
    # Usar a chamada POST do digisac para enviar a mensagem para o chamado
    'com a variavel "chamado_id" '

# Logica do processador de fila

# Pegar lista


def processar_filas():
    print('INICIANDO O PROCESSADOR DE FILAS...\n')


lista_bruta = buscar_chamados_triagem
# buscar_chamados_triagem sera os chamados adquiridos pelo digisac
'apartir do json.'

# 'deque' para usar uma fila eficiente
fila_de_chamados = collections.deque(lista_bruta)
print('\nLista de chamados pronta.\nTotal : {}'.format(len(fila_de_chamados)))

print('Chamados na fila :\n {}\n'.format(list(fila_de_chamados)))

# Lopp para processar enquanto não houver 3 disparos por cliente
'e outro loop para processar os chamados enquanto houver na fila'
contador_disparos = 0

while (contador_disparos < 3):
    contador_disparos += 1
    while (fila_de_chamados):
        print('Iniciando um lote para disparo...\n')
        disparo_atual = []

        # Montar o lote ate o tamanho maximo de 13
        for _ in range(TAMANHO_DO_DISPARO):
            if not fila_de_chamados:
                break
            chamado = fila_de_chamados
            disparo_atual.append(chamado)

            # Executando disparos
            print('Executando {} chamados neste lote'.format(
                len(disparo_atual)))
            # chamado id também coletado da apartir do digisac com json
            for chamado_id in disparo_atual:
                sucesso = enviar_disparo_chamados(chamado_id)
                if not sucesso:
                    print(
                        '[ERRO] Falha ao enviar chamado {}'.format(chamado_id))

                    # Informar os que vão ser enviados e os que vão aguardar o proximo lote
                    print('RELATORIO\n')
                    print('Lista de chamados enviados agora {}\n'.format(
                        len(disparo_atual)))
                    print('Chamados aguardando nafila : {}'.format(
                        len(fila_de_chamados)))
                    if fila_de_chamados:
                        print('Proximos a serem enviados: {}'.format(
                            list(fila_de_chamados)))
                        tempo_de_pausa_fila = time.sleep(
                            random.randint(PAUSA_MINIMA_FILA, PAUSA_MAXIMA_FILA))
                        print('Pausa para o proximo lote da fila de triagem {:.2f}'.format(
                            tempo_de_pausa_fila))

    # Looping para fazer  segundo e terceiro após os 30 a 60 min de espera apartir da lista
    # de represados do digisac
    while (contador_disparos > 1):
        tempo_de_pausa_disparo = time.sleep(random.randint(
            PAUSA_MINIMA_DISPARO, PAUSA_MAXIMA_DISPARO))
        print('Pausa para o proximo disparo {:.2f}'.format(
            tempo_de_pausa_disparo))
        # buscar_chamados_represados sera os chamados adquiridos pelo digisac
        lista_bruta_represados = buscar_chamados_represados
    # apartir do json
        fila_de_represados = collections.deque(lista_bruta_represados)
        print('\nLista de represados pronta.\nTotal : {}'.format(
            len(fila_de_represados)))

        print('Represados na fila :\n {}\n'.format(list(fila_de_represados)))

        print('Iniciando lote para segundo disparo...\n')
        disparo_atual_represados = []
        for _ in range(TAMANHO_DO_DISPARO):
            if not (fila_de_represados):
                break
            chamado_represado = fila_de_represados
            disparo_atual_represados.append(chamado_represado)
            print('Executando {} disparos desse lote de represados:'.format(
                len(disparo_atual_represados)))
            for chamado_id in disparo_atual_represados:
                sucesso2 = enviar_disparo_represados
                if not sucesso:
                    print('[Erro] Falha ao enviar represado {}'.format(chamado_id))

                    print('Total de represados enviados agora {}'.format(
                        len(disparo_atual_represados)))
                    print(
                        f'Total de represados aguardando na fila para o {contador_disparos} disparo : {len(fila_de_represados)}')
                    print('Proximos na fila {}'.format(
                        list(fila_de_represados)))

input('Pressione Enter para encerrar o programa...')
