def funcion_de_3_cifras(lista):
    """ funcion para crear una nueva lista en base
    a si 1 o 3 valores cumplen con estar dentro del
    rango estipulado"""
    lista_de_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            lista_de_cifras.append(numero)
        else:
            pass
    return lista_de_cifras


resultado = funcion_de_3_cifras([207, 10, 600])
print(resultado)


# Section Test 1
def todos_positivos(lista_de_numeros):
    for numero in lista_de_numeros:
        if numero <= 0:
            return False
    return True


lista_numeros1 = [2, -3, 4, -5]
resul = todos_positivos(lista_numeros1)
print(resul)


# Section Test 2
def suma_menores(lista):
    suma = 0
    for numero in lista:
        if numero in range(0, 1000):
            suma += numero
        else:
            pass
    return suma
# otra manera de hacerlo: return sum(num for num in lista if 0 < num < 1000)


lista_numeros = [10, 345, 200, 1500, -5]
resultaek = suma_menores(lista_numeros)
print(resultaek)


# Section Test 3
def cantidad_pares(lista_pares):
    total_pares = []
    for numero in lista_pares:
        if numero % 2 == 0:
            total_pares.append(numero)
        else:
            pass
    return len(total_pares)


lista_numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado3 = cantidad_pares(lista_numeros3)
print(resultado3)


