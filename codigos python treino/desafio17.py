import math
cateto_oposto = int(input('Insira o valor do cateto oposto\n>>'))
cateto_adjacent = int(input('Insira o valor do cateto adjacente\n>>'))
hipotenuza = math.sqrt(cateto_oposto**2 + cateto_adjacent**2)
print('O valor da hipoteusa deste triangulo ={:.2f}'.format(hipotenuza))
