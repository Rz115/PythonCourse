'''Solo funciona para traer el valor miniomo y maximo en cualquier tipo de dato'''
numeros = [34, 56,63,77,23]
print(min(numeros))

print(f'El valor mínimo es {min(numeros)} y el valor máximo es {max(numeros)}')

#Otro ejemplo:

listaek = ["Pedro","Diegol","Raul","Alicia"]
print(min(listaek))

#otro ejemplo:
nombre = "Carlangas"
print(min(nombre.lower()))

#igual en diccionarios:
diccionario = { 'C1':45, 'C2':11, 'A3': 90}
print(min(diccionario))
print(min(diccionario.values())) ; #Esto solo es si quisiera el minimo de los valores

#Section test 1:
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

#Section test 2:
lista_numeros1 = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
valor_maximo1 = max(lista_numeros1)
valor_minimo1 = min(lista_numeros1)
rango = valor_maximo - valor_minimo1
print(rango)

#Section test 3:
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)