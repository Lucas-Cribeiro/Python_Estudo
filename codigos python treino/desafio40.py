nota_1 = float(input('Insira a primeira nota do aluno\n>> '))
nota_2 = float(input('Insira  a segunda nota do aluno\n>>'))
media = (nota_1 + nota_2) / 2
if media < 5.0:
    print(
        f'REPROVADO!\nMédia minima não atingida, sem direito a recuperação.\nMÉDIA FINAL: {media:.1f}')
elif media >= 5.0 and media < 7.0:
    print(
        f'RECUPERAÇÃO!\nAluno não atingiu a média para ser aprovado, mas tem direito a recuperação.\nMÉDIA FINAL : {media:.1f}')
else:
    print(f'APROVADO!\nAluno aprovado na materia.\nMÉDIA FINAL: {media:.1f}.')
