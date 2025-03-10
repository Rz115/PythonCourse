#analizador de texto
#Crear un programa que le pida un texto al usuario, luego pedir al cliente que asigne 3 letras al azar y de ahí imprimir lo siguiente:

'''
1..- ¿Cuántas veces  aparece cada una de las letras que eligió?
2.- ¿Cuántas palabras hay en total de ALL el texto?
3.- ¿Cuál es la primera y la ultima letra del texto? - indexacion
4.- ¿Cómo invertir el orden de las palabras?
5.- Decir si la palabra Python se encuentra dentro del texto
'''

print("Bienvenido al analizador de texto de RAULH\n")
resultado = input("Por favor introduce el texto que desees: ")
letra1 = input("Introduce a continuación UNA letra random, puede ser mayúscula ó minúsucla: ")
letra2 = input("Introduce a continuación una SEGUNDA letra random, puede ser mayúscula ó minúsucla: ")
letra3 = input("Introduce a continuación una TERCERA letra random, puede ser mayúscula ó minúsucla: ")

#Aqui almacenamos las 3 letras en una lista
lista_de_letras = [letra1, letra2, letra3]

#Aqui convertimos las tres letras a minuscula
resultado1 = resultado.lower()
letra_1 = lista_de_letras[0].lower()
letra_2 = lista_de_letras[1].lower()
letra_3 = lista_de_letras[2].lower()

#Cuantes veces aparece la primer letra
variable1 = resultado1.count(letra_1)

#Cuantes veces aparece la segunda letra
variable2 = resultado1.count(letra_2)

#Cuantes veces aparece la tercera letra
variable3 = resultado1.count(letra_3)

'''CASO UNO COMPLETADO'''
print(f"\n\tTu primer letra seleccionada fue \'{letra1}\', esta letra se repite: {variable1} vez/veces dentro del texto")
print(f"\tTu primer letra seleccionada fue \'{letra2}\', esta letra se repite: {variable2} vez/veces dentro del texto")
print(f"\tTu primer letra seleccionada fue \'{letra3}\', esta letra se repite: {variable3} vez/veces dentro del texto")

'''CASO DOS COMPLETADO'''
resultado2 = resultado.split()
print(f"\tEl total de caracteres que conforma tu texto es de: {len(resultado2)}")

'''CASO TRES COMPLETADO'''
resultado3 = resultado[0]
print(f"\tLa primera letra o caracter que conforma tu texto es: {resultado3}")
resultado35 = resultado[-1]
print(f"\tLa ultima letra ó caracter que conforma tu texto es: {resultado35}")

'''CASO CUATRO COMPLETADO'''
resultado4 = resultado.split()
resultado4.reverse()
dereversa = " ".join(resultado4)
print(f"\tEl texto que introduciste a la inversa quedaría así:\n \t \"{dereversa}\"")

'''CASO CINCO COMPLETADO'''
confirmacion = "python" in resultado
dic = {True: "si", False: "no"}
print(f"\tLa palabra Python se encuentra o no dentro del texto introducido: {dic[confirmacion]}")

'''Otra manera de hacerlo:
letras []
letras.append(input("Introduce a continuación UNA letra random, puede ser mayúscula ó minúsucla: ").lower())

'''