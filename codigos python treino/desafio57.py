sexo = str(input('Insira "M" para sexo masculino e "F" para feminino.\n>>')).upper()
while (sexo != "M") and (sexo != "F"):
    sexo = str(input(
        'Digitação inválida. Selecione novamente "M" para masculino ou "F" para feminino.\n>>')).upper()
if sexo == "M":
    print('Seu sexo : Masculino')
else:
    print('Seu sexo: Feminino')
