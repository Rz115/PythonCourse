diccionario = {'clave1': 'agua', 'clave2': 34}
a = diccionario.popitem()
print(a)

#ejercicio 1:
textoek = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
ejemplo = textoek.lstrip(",:_#%") #remueve solo los caracteres de la izquierda?
print(ejemplo)

#ejercicio 2:
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"Naranja")
print(frutas)

#ejercicio 3:
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

''' isdisjoint() ->  Return True if the set has no elements in common with other. 
Sets are disjoint if and only if their intersection is the empty set.'''