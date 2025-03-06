'''Como en javascript u otros lengujaes el tipico Switch, case de Python sería el siguiente:
A partir de la actualizacion 3.10 de python se incluyó, antes se usaba if, elif, etc... '''

serie = "N03"
match serie:
    case "N01":
        print("Motorola")
    case "N02":
        print("Samsung")
    case "N03":
        print("Nokia")
    case _:
        print("No existe el numero de serie")

'''Otro ejemplo practico, esta vez incluyendo 2 diccionario y uno de ellos 
incluye como segunda clave otro diccionario'''

cliente = {'nombre': 'Raul',
           'edad': 30,
           'ocupacion': 'Desarrollador'}
pelicula = {'titulo': 'matrix',
            'Ficha_tecnica': {'protagonista': 'Keanu Reeves',
                              'director': 'Lana & Lily'}}
elementos = [cliente, pelicula, 'libro'] #Este valor de string solo fue utilizado para poder recorrer la lista completa

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'Ficha_tecnica': { 'protagonista': protagonista,
                                 'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            "Esto no es relevante"


