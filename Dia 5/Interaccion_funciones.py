from random import *
# lista inicial
palitos = ['-', '--', '---', '----']


# mezclar elementos de lista o funcion para hacerlo
def mezclar(lista):
    shuffle(lista)
    return lista


# funcion para seleccionar elemento mezclado
def probar_suerte():
    intento = ''
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Por favor elige un número del 1 al 4: ")

    return int(intento)


# comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Te toca lavar los trastes banda")
    else:
        print("Te salvaste de lavar los platos we")

    print(f"Te ha tocado éste palitoek: {lista[intento - 1]}")


# Aquí todavía no se ejecuta nada, solo se crearon las funciones, abajo se invoca cada una en una variable
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


# Ejercicio 1
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(lanzar1, lanzar2):
    suma_dados = lanzar1, lanzar2
    if lanzar1 + lanzar2 <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable.")
    elif 6 < lanzar1 + lanzar2 < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances.")
    elif lanzar1 + lanzar2 >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parace una jugada ganadora.")

    return suma_dados


dato1, dato2 = lanzar_dados()
suma = evaluar_jugada(dato1, dato2)
print(suma)

# Ejercicio 2

# Ejercicio 3



