#Operadores logicos
'''comparacion directa'''
mi_variable = 1<9<6
print(mi_variable)

'''comparacion con metodo AND obligatoriamente deben cumplirse AMBOS requerimientos'''
mi_bool = (5 == 5) and ('perro' == 'perro')
#print(mi_bool)

'''comparacion con metodo OR  obligatoriamente deben cumplirse aun que sea UNO de los 2 requerimientos'''
mi_bool = (10 == 19) or (3 == 3)
#print(mi_bool)

texto = "Esta frase es breve"
mi_bool = ('frase' in texto) and ('breve' in texto)
#print(mi_bool)

'''comparacion con metodo NOT '''
mi_bool = 'a' not in texto
#print(mi_bool)
''' queremos saber lo contrario a lo que tenga la información, por eso la operacion de abajo es verdera'''
mi_bool2 = not ('a' != 'a')
print(mi_bool2)