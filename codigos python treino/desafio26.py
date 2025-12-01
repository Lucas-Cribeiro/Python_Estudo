texto = input('Insira uma frase da sua escolha\n>>')
texto_minus = texto.lower()
qntd_a = texto_minus.count('a')
posicao_a = texto_minus.find('a')
posicao_final_a = texto_minus.rfind('a')
print(f'A letra "a" aparece {qntd_a} vezes na frase')
print(
    f'A letra "a" aparece pela primeira vez na posição {posicao_a} nesta frase.')
print(f'A posição do ultimo "a" no texto é {posicao_final_a}.')
