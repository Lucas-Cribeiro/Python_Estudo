import random
aluno1 = (input('Insira o nome do primeiro aluno\n>>'))
aluno2 = (input('Insira o nome do segundo aluno\n>>'))
aluno3 = (input('Insira o nome do terceiro aluno\n>>'))
aluno4 = (input('Insira o nome do quarto aluno\n>>'))
lista = [aluno4, aluno1, aluno2, aluno3]
random.shuffle(lista)
print('A sequência de apresentação sera: {}'.format(lista))
