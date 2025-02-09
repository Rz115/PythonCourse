# Imprimir string simple
variablename = "Raul"
#print(variablename)
#Tipos de datos y reglas:
# - String, integer, float
# Tienes ahora colecciones de datos como:
# - list o lista que tienen un orden y un indice pero son mutables (hay métodos que te permiten reordenar los elementos de una lista) y se usan corchetes
# - dic o diccionario (como un objeto en javascript con clave y valor y se usan llaves estos no llevan un orden),
# - Tuples ó tup (son con paréntesis igual que las listas pero NO se pueden modificar el orden)
# - Sets ó set, conjunto de elementos ordenados ÚNICOS. Las listas y los tuples pueden tener elementos repetidos, PERO LOS SETS NO

# Imprimiendo integer con string
edad = 30
edad2 = 15
edades = edad + edad2
#print(f"La operacion resultante de edad y edad2 es: {edades}")

# Imprimiendo variable dentro de una entrada de dato
#nombre = input("Dime tu nombre: ")
#print("Tu nombre es " + nombre)

# Regla 1: legible, Regla 2: unidad, Regla 3: hispanismos, Regla 4: numeros en nombre de variable al final
# Regla 5: No signos al nombrar variables, Regla 6: Palabras clave y no similar a tu codigo

numerorandom = 30.6
#print(type(numerorandom))
#Como resultado será string, por que las entradas input siempre son string
#edaddenuevo = input("Dime tu edad: ")
#print(edaddenuevo+edaddenuevo)

#existen dos tipos de conversiones/casting : implicitas y explicitas
#Conversiones implicitas por el sistema:
num1 = 20
num2 = 30.5
num1 = num1 + num2
#print(num1)

#Conversiones explicitas cambiando de float a integer
numero1 = 5.8
#print(numero1)
#print(type(numero1))

numero2 = int(numero1)
#print(numero2)
#print(f"Convertir el primer numero1 de float a integer resulta en: {type(numero2)}")

#edad = input("Dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
#print(nueva_edad)
#incorrecto hacer esto siguiente:
#print("Tu nueva edad es: " + nueva_edad)

#Imprimir cadenas de datos de cualquier tipo
#formatear cadenas
x = 10
y = 5
#manera old
#print("Mis numeros son " + str(x) + " y " + str(y))
#manera 1 funcion format
#print("Mis numeros son  {} y {}".format(x,y))
print("La suma de {} y  {} es igual a {}".format(x,y,y+x))
#Segunda manera de hacerlo llamadas CADENAS LITERALES"
color = "Azul"
matricula = 16456450
print(f"\nEl auto es {color} y su matricula es {matricula}\n")

numeroek1 = 7.5
numeroek2 = 2.6
suma = numeroek1 + numeroek2
#print(type(suma))

num1 = "7.5"
num2 = "10"
#print(float(num1) + int(num2))

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_nuevos + puntos_anteriores
#print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

nombre_asociado = "Raul Martos"
numero_asociado = 13560339
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")