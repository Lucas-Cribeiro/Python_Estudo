frase = input('Insira uma frase para verificarmos se é um políndromo ou não. Escreva sem ascentos e sem pontuação, apenas espaço e palavras.\n>> ')
frase_sem_esapco = frase.replace(" ", "").upper()
frase_invertida = frase_sem_esapco[::-1]
if frase_invertida == frase_sem_esapco:
    print(f'A frase {frase} é um políndromo .')
else:
    print(f'A frase {frase} não é um políndromo.')
