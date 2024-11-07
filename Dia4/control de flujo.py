'''if 10 > 19:
    print('Es correcting')
else:
    print('Incorrecting')'''

#otro ejemplo:

'''mascota = 'conejo'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'pez':
    print('Tienes un pez')
elif mascota == 'perro':
    print('Tienes un perrazo')
else:
    print('No sé que animal tienes')'''


#Anindando condiciones if
edad1 = 16
calificacion = 9

'''if edad1 < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('NO aprobado')
else:
    print('Eres adulto')'''


'''EJERCICIO 1'''
edad = 16
tiene_licencia = False

if edad >= 18:
    print("Puedes conducir")
elif tiene_licencia == True:
    print("No puedes conducir aún. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")



'''EJERCICIO 2'''
habla_ingles = True
sabe_python = False

if habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif sabe_python == False:
    print("Para postularte, necesitas saber programar en Python")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
else:
    print("Cumples con los requisitos para postularte")


