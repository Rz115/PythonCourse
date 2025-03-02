'''basicamente le otorga un indice a una collecion de datos y entrega cada elemento de la misma
en tuples con su indice este es el primer ejemplo:'''
lista = ['a','b','c','d']
for item in enumerate(lista):
    print(item)

'''de la misma forma pero más "elegante" al incluir como parámetro al indice
y luego al item dentro de la lista, este es el segundo ejemplo:'''
lista = ['a','b','c','d']
for indice,item in enumerate(lista):
    print(indice,item)

'''Puedes crear una lista de tuples haciendo un casting (cambiar formato de tipo de dato)
 y desempacar los datos dentro de los mismos tuples, este es el tercer ejemplo:'''
lista = ['a','b','c','d']
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])


#section test 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
mis_tuples2 = list(enumerate(lista_nombres))
for indice,nombre in mis_tuples2:
    print(f'{nombre} se encuentra en el índice {indice}')

#section test 2
lista = ['P','y','t','h','o','n']
lista_indices = list(enumerate(lista))
print(lista_indices)

#section test 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(indice)


