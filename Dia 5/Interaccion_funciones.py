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

    print(f"Te ha tocado éste palitoek: {lista[intento - 1]}\n")


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
    suma_dados = lanzar1 + lanzar2
    if suma_dados <= 6:
        resultado = f"La suma de tus dados es {suma_dados}. Lamentable."
    elif 6 < suma_dados < 10:
        resultado = f"La suma de tus dados es {suma_dados}. Tienes buenas chances."
    elif suma_dados >= 10:
        resultado = f"La suma de tus dados es {suma_dados}. Parace una jugada ganadora."

    return resultado


dato1, dato2 = lanzar_dados()
suma = evaluar_jugada(dato1, dato2)
print(suma)

# Ejercicio 2
lista_numeros = [1, 2, 7, 10]


def reducir_lista(listadevolver):
    sin_duplicados = list(set(listadevolver))
    sin_duplicados.remove(max(sin_duplicados))
    return sin_duplicados


def promedio(listadev):
    promedioek = 0
    total = len(listadev)
    for numero in listadev:
        promedioek += numero
    average = promedioek / total
    return average


lista_reducida = reducir_lista(lista_numeros)
pro = promedio(lista_reducida)
resultado = f"el promedio de la lista es {pro}"

# Ejercicio 3
lista_numeros = [1, 2, 3, 4, 5]


def lanzar_moneda():
    return choice(['Cara', 'Cruz'])


def probar_suerte(lanzamiento, lista):
    if lanzamiento == 'Cara':
        lista.clear()
        print("La lista se autodestruirá")
        return lista
    else:
        print("La lista fue salvada")
        return lista


monedalanzada = lanzar_moneda()
resultado = probar_suerte(monedalanzada, lista_numeros)
print(resultado)




