#Loop definida de iteraciones : FOR
nombres = ['Raul', 'Jack', 'Paulina', 'Maribel']

for element in nombres:
    numero_de_nombres = nombres.index(element) + 1
    print(f"Nombre {numero_de_nombres}: {element}")

#Otro ejemplo
lista = ['Raul', 'Jack', 'Celeste', 'Maribel', 'Carmen', 'Paulina']
#Puedes mezclar métodos, en este caso lo aplique ya que los nombres se escriben con
#mayúsculas y sin el metodo lower no me entrega nombres a menos que fuésen minusculas
for nombres_nuevos in lista:
    if nombres_nuevos.lower().startswith('c'):
        print(nombres_nuevos)
    else:
        print("Nombre que no comienza con \'C\' \n")


#Otro ejeemplo
numeros = [1,2,3,4,5]
mi_valor = 0
#Recorre toda la lista y al finalizar imprime el valor total fuera del for
for numerosek in numeros:
    mi_valor = mi_valor + numerosek
#Print fuera del loop por que no sigue la misma sangría que lo que esta dentro.
print(mi_valor)


#Otro ejemplo
palabra = 'pythones\n'
for letra in palabra:
    print(letra)

#ó también:
for letra2 in 'python\n':
    print(letra2)

#ó también con una lista o un tuple ó una lista que contenga listas:
for letra3 in (1,2,3,4):
    print(letra3)

#ó también:
for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

#creas parametro para sacar elementos de listas dentro de la lista:
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

#ahora iterar en un diccionario:
for item in {'llave1':'a', 'llave2':'b', 'llave3':'c'}:
    print(item)

#normalmente
diccionario = {'clave1':'do', 'clave2':'re', 'clave3':'mi'}
for item in diccionario.values():
    print(item)


# imprimir solo valores por clave en el diccionario:
for a,b in diccionario.items():
    print(a,b)

#little test
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero

print(suma_numeros)

#another little test
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for element in lista_numeros:
    if element % 2 == 0:
        suma_pares = suma_pares + element
    else:
        suma_impares = suma_impares + element

print(suma_pares)
print(suma_impares)