''' Cómo importar métodos a Python, para que el lenguaje entregue un numero al azar
puedes importar diferentes métodos de una libreria y puden verse asi:
from random import randint '''

from random import *

aleatorio = randint(1,50)
print(aleatorio)
#metodo uniform para entregar valores random pero flotantes, podemos redondearlo con round
aleatorio = round(uniform(1,5),2)
print(aleatorio)
#metodo random para entregar valores random pero para entregar fraccion entre 0 y 1
aleatorio = random()
print(aleatorio)
#metodo choice para entregar valores random pero un rango de strings en una lista por ejemplo:
colores = ['Azul','Amarillo','Verde','Rojo','Morado']
aleatorio = choice(colores)
print(aleatorio)
#metodo shuffle para entregar valores revueltos, por ejemplo en una lista usa los mismos valores
# pero los revuleve cada vez que se imprime, NO SE PUEDE usar con strings
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

#Section test 1:
ale = randint(1,10)
print(ale)

#Section test 2:
alek = random()
print(alek)

#Section test 3:
nombres1 = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres1)
