#Más metodos para strings en python
#index, format, upper, lower, split, join, find, replace

#metodo para convertir string en solo mayusculas o utilizar un index igual para hacerla mayuscula como guste
texto = "Este es un texto nuevo"
#resultado = texto.upper()
resultado = texto[2].upper()
print(resultado)
#metodo para convertir string en solo minusculas o utilizar un index igual para hacerla minuscula como guste
texto = "Este es un texto nuevo"
resultado = texto.lower()
print(resultado)
#metodo separar un string en elementos y los guarda dentro de una lista
texto = "Este es un texto nuevo"
resultado = texto.split()
print(resultado)

#metodo separar un string en elementos y los guarda dentro de una lista PERO determinando criterio de separacion que va a tener dicha lista con split
texto = "Este es un texto de Raul"
resultado = texto.split("t")
print(type(resultado))
print(resultado)

#DATO IMPORTANTE: LAS LISTAS SE GUARDAN CON CORCHETES [] Y LOS DICCIONARIOS CON LLAVES {}

#Metodo para unir, lo contrario a split
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print(e)
#ó también
j = "-".join([a, b, c, d])
print(j)

#Metodo find, sirve igual que index, la unica diferencia es que si no se encuentra el caracter o palabra dentro del string te retornará un -1
texto = "Vamos a aprender muchas cosas con Python"
impresion = texto.find("desk")
print(impresion)
#o como index
texto = "Vamos a aprender muchas cosas con Python"
impresion = texto.find("muchas")
print(impresion)


#Metodo  replace para tomar fragmento del texto del string y reemplazarlo por otro, necesita 2 parametros
texto = "Vamos a aprender muchas cosas con Python"
res = texto.replace("aprender", "comida")
res2 = res.replace("cosas", "buenas")
print(res2)
#O remplazar todas las letras e por una x
#Metodo  replace para tomar fragmento del texto del string y reemplazarlo por otro, necesita 2 parametros
texto = "Vamos a aprender muchas cosas con Python"
res = texto.replace("e", "x")
print(res)

''' Los metodos actuan en el lugar (in place) modifican los objetos directamente, sin retornar nungun otro dato mas que la propia accion
 (por ello, si intentamos asignarlos a variables, las mismas quedarán vacías) '''