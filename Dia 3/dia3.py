#indice
mi_texto= "Esta es una prueba"
resultado = mi_texto[3]
print(resultado)
#indice pero ubicar un caracter en un string
mi_texto= "Esta es otra prueba"
resultado2 = mi_texto.index("a", 5, 12)
print(resultado2)
#otro metodo rindex es indice de derecha a izquierda, la izquierda siempre comienza con un 0
mi_texto= "Esta es otra prueba"
resultado3 = mi_texto.rindex("a")
print(resultado3)

#forma de fragmentar o slicing nuestros strings:
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10]
print(fragmento)
#fragmentando por palabra completa, por ejemplo:
textoek = "Esta palabraek será extraída"
fragmentoek = textoek[5:14]
print(fragmentoek)

#forma de fragmentar o slicing nuestros strings, el tercer factor extrae de forma en las partes que quieres que se divida:
texto = "faertysdfggfxvcnggtrewsd"
fragmento1 = texto[2:10:2]
print("Este es el primer fragemento: "+ fragmento1)

#MAS FORMAS DE FRAGMENTAR:
texto = "MIDOGKRUEISKALAPLE"
#Asi toma del caracter 2 al final del string
fragmento2 = texto[2:]
print("Este es el segundo fragemento: "+ fragmento2)

#Asi toma del caracter -2 al principio del string
fragmento3 = texto[:-2]
print("Este es el tercer fragemento: "+ fragmento3)

#Asi toma del caracter en la posición -3 hasta el principio del string pero cada 3 caracateres
fragmento4 = texto[::-3]
print("Este es el cuarto fragemento: "+ fragmento4)
#así toma toma caracteres cada tres espacios
fragmento5 = texto[::3]
print("Este es el quinto fragemento: "+ fragmento5)

#iNVIERTES TODOS los caracteres de esta manera
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print("La frase invertida diría: "+ frase[::-1])


texto5 = "COMIDA"
fragmento6 = texto5[:-1]
print(fragmento6)
