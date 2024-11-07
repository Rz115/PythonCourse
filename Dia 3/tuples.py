'''son similares a las listas pero son inmutables, llevan parentesis, ó sin encerrarlos en nada y funcionan igual
ocupan menos espacio de memoria que las listas y se procesan más rapido
al no poder ser modificadas se usan en situaciones para almacenar estructuras que no desamos sean modificadas'''
taples = (1,2,3,4)
print(type(taples))

#INdexar
print(taples[-2])
'''tener tuples con todo tipo de objeto'''
t = (5, 4.5, 'Francisco', (10, 20, 30), 8)
print(t[3][0])

#hacer castings
mi_tuple = (5, 4.5, 'Francisco', (10, 20, 30), 8)
mi_tuple = list(mi_tuple)
print(mi_tuple)

'''tener tuples con todo tipo de objeto'''
test = (5, 4.5, 'Francisco', (10, 20, 30), [2, 3, 'comida'], {'c1': 'Raul', 'c2':'Martos', 'c3': 27})


#agregar contenido a un tuple
tap = (1, 2, 3)
x, y, z = tap
print(x, y, z)

#metodo para conocer cantidad de apariciones de un tuple
taps = (1, 2, 3, 1, 4, 1)
print(taps.count(1))
#se observa arriba que el 1 aparece 3 veces


#metodo para conocer cantidad de apariciones de un tuple
taps = (1, 'Francisco', 3, 'Francisco', 4, 1)
print(taps.count('Francisco'))



#metodo para conocer el index en el que se encuentra un item dentro del tuple
taps2 = (1, 6, 8, 1, 5, 6)
print(taps2.index(8))
#se observa arriba que el 8 esta en la posicion 2 del tuple