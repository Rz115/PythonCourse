"""Sustituye la cantidad corta de parametros y añade con el *(y el nombre args que es mas
común) una cantidad variable de argumentos, por ejemplo en lugar de no saber si vas
a sumar solo dos numeros ó son más de 2 se podría utilizar..."""


def suma(*args):
    return sum(args)


print(suma(2, 2, 4, 5, 6, 7, 100, 150))

# Seccion test 1:

# Section test 2:

# Section test 3:


