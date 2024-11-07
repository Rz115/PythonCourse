''' Los sets son coleccion de elementos como listas se pueden declarar de dos maneras
set () ó usando llaves {} sin usar set,  la primera forma necesita llevar encerrado los elementos
ya sea con llaves, parentesis, corchetes, etc. PERO SOLO  si usas de esta menera los sets: set()
En cambio, si se creo el set sin la palabra como tal y solo con las llaves entonces puedes poner todos los elementos
directamente, motivo de uso de los sets es por que solo admiten elementos únicos, los elementos no se repiten
Los elementos no estan ordenados en indices, no puedes indexarlos ni actualizar ni nada, SON inmutables. Si puedes almacenar
elementos de diferentes tipos de datos pero NO listas y NO diccionarios
'''
#Primera manera de componerlos
mi_set = set([2, 4, 6, 8])
'''print(type(mi_set))
print(mi_set)'''

#Segunda manera de ejecutar un set
mi_set2 = {1, 2, 3, 4, 5}
'''print(mi_set2)
print(type(mi_set2))'''


#LOS elementos repetidos se eliminan
mi_set3 = set([2, 4, 6, 8, 2, 4, 5 , 3, 1, 2, 3, 4])
'''print(type(mi_set3))
print(mi_set3)'''

#no acepta listas o diccionarios pero si tuples
mi_set4 = set([2, 4, 6, 8, (2, 3, 4), 5 , 3, 1, 2, 3, 4])
'''print(type(mi_set4))
print(mi_set4)'''

#puedes hacer este tipo de busqueda mientras conozcas las claves
miset5 = set((1, 2, 3, 4, 5, 6, 7, 8, 9))
'''print(2 in miset5)'''

#Union   de sets
s1= {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
#print(s3)

#METODO add  or update, pero si es el mismo valor existente no lo tomará en cuenta el sets
s1= {1, 2, 3}
s1.add(4)
#print(s1)

#metodo para borrar
'''s1.remove(3)
print(s1)'''

#metodo para descartar, la diferencia es que no dará error como eliminar
s1.discard(6)
#print(s1)

#metodo para descartar UN elemento aleatoriamente de un set, ya que no tienen orden
s1= {1, 2, 3, 4, 5}
#sorteo = s1.pop()
#print(sorteo)

#metodo para vaciar nuestro set
s1= {1, 2, 3, 4, 5}
s1.clear()
print(s1)