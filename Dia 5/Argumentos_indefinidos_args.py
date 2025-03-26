"""Sustituye la cantidad corta de parametros y añade con el *(y el nombre args que es mas
común) una cantidad variable de argumentos, por ejemplo en lugar de no saber si vas
a sumar solo dos numeros ó son más de 2 se podría utilizar..."""


def suma(*args):
    return sum(args)


print(suma(2, 2, 4, 5, 6, 7, 100, 150))


# Seccion test 1:
def suma_cuadrados(*args):
    lista = []
    for numero in args:
        nuevo_valor = numero**2
        lista.append(nuevo_valor)
    return sum(lista)


resultado = suma_cuadrados(1, 2, 3, 4)
print(resultado)


# Section test 2:
def suma_absolutos(*args):
    suma_numeros = sum(map(abs, args))
    return suma_numeros


resulta2 = suma_absolutos(1, -2, 3, -4, 5)
print(resulta2)


# Section test 3:
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona('Pedro', 75, 65, 300))


