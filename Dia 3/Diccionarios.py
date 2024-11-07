'''Diccionario es una colecccion de datos pares concepto y valor asociado se usan llaves y las claves
no pueden repetirse, no tienen un indice u orden específico
las claves no se pueden repetir, tienen que ser unicas, los valores si pueden repetirse '''
diccionario = {'c1': 'valor1', 'c2': 'valor2'}
#busquedas por claves
result = diccionario['c1']
print(result)

cliente = {'nombre': 'Juan', 'apellido': 'Mendoza', 'peso': 78, 'talla': 1.76}
consulta = (cliente['apellido'])
print(consulta)

#diccionario dentro de diccionario
dic = {'c1':55, 'c2':[10,20,'comida'], 'c3':{'s1':100, 's2':70, 's3': 'equisde'}}
#print(dic['c2'][1])
print(dic['c3']['s2'])

#ejercicio para buscar un valor en un diccionario con dos listas y volver dicho valor en mayuscula
diccionarioejercicio = {'d1': ['a','b','c'], 'd2':['d','e','f']}
print(diccionarioejercicio['d2'][1].upper())


#modificar en el lugar el diccionario
dic4 = {1:'a', 2:'b'}
print(dic4)
dic4[3] = 'c'
print(dic4)

#sobreescribir un valor existente
dic4[2] = 'B'
print(dic4)

#finalmente metodo keys para traer todas las claves del diccionario
print(dic4.keys())
#finalmente metodo values para traer todos los valores del diccionario
print(dic4.values())
#finalmente metodo para conocertodo lo que hay en un diccionario
print(dic4.items())
