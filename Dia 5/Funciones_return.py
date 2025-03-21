def multiplicar(numero1, numero2):
    total = numero1 * numero2
    return total


operacion = multiplicar(6, 3)
print(operacion)


# Section Test 1
def potencia(num1, num2):
    resultado = num1**num2
    return resultado


pote = potencia(3, 4)
print(pote)


# Section Test 2
def usd_a_eur(dolar):
    return dolar * 0.90


dolares = usd_a_eur(2)
print(dolares)


# Section Test 3
def invertir_palabra(palaek):
    return palaek[::-1].upper()


palabra = invertir_palabra("Python")
print(palabra)