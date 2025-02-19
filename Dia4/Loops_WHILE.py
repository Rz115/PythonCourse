#Estructura while básica
monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -=1
else:
    print("No tengo más dinero")

#Otro ejemplo de que son loops indefinidos o pueden ser finitos dependiendo el usuario:
'''respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Quiéres seguir? (s/n): ")
else:
    print("Gracias")'''


#Otro ejemplo con palabras CLAVE : PASS:
'''respuestaek = 's'
while respuestaek == 's':
    pass'''

print("Hola mundo voy a seguir programando acá, luego sigo trabajando con el while arriba")

#Otro ejemplo con palabras CLAVE : BREAK:
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#Otro ejemplo con palabras CLAVE : CONTINUE:
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)

#little test including module operator
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1

#another little test
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)

