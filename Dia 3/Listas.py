'''Una lista es una secuencia ordenada de objetos, compuesta con diferentes tipos de datos, entre corchetes,
listas dentro de listas, indexarlas, fraccionarlas, etc '''
mi_lista = ['comida', 'b', 'C', 5, 66, 23]
resultado = len(mi_lista)
#print(resultado)
print(mi_lista)

#indexar tambien una lista , buscar caracter o recorrer una lista
resultado2 = mi_lista[0]
resultado3 = mi_lista[0:4]
print(resultado3)

#Concatenacion
mi_lista2 = ["d", "e", "F", 90]
mi_lista3 = mi_lista + mi_lista2
#print(mi_lista3)

#cambiar un elemento
mi_lista3[0] = 'alfa'
print(mi_lista3)

#agregar elemento
mi_lista3.append('g')
#print(mi_lista3)

#eliminar elemento
#mi_lista3.pop(0)
#print(mi_lista3)

#eliminar elmento Y guardamos el elemento eliminado en una variable asi:
reserva = mi_lista3.pop(0)
#print(mi_lista3)
#print(reserva)

#ordenar la lista, metopdo sort y otros no forzosamente devuelven algo al imprimir, simplemente hacen algo con la lista o var y ya
lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()
print(lista)

#cambiar el orden, lo ultimo primer
lista.reverse()
print(lista)

#dato extra solamente visto en internet en unn quiz para ordenar inexadamente
print("{2}, {1}, {0}".format(*"abc"))


letra1 = 'A'
letra1 = 'z'
letra1 = 'C'
#Aqui almacenamos las 3 letras en una lista
letras = [letra1, letra1, letra1]

listas = ['in', 'as', 'if', 'be']
print(listas[1:][:2])
