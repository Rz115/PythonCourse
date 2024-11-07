#Esto no se puede ya que los strings son inmutables
nombre = "Carina"
#nombre[0] = "K"
#print(nombre)

#Concatenacion de 2 strings en uno
n1 = "Kari"
n2 = "na"
print(n1+n2)

#Strings se pueden multiplicar
n1 = "Die"
print(n1*10)

#Sstrings grandes con salto de linea
n5 = """SOL es iluminativo para la vida humana
fsdfsddsfsfsdgdfjytrytr
ffasdfsdfsdfds
sdfhfsdghbfdgbhxgh
sdhfghfghgf
fsdfsdgfhfghfgh
fsdfs
dfssdf
dshfghgfht"""

print(n5)

#Consultar si en un string existe una detrminada palabra o caracter
print("agua" in n5)
print("iluminativo"  in n5)
print("iluminativo" not in n5)

#len te permite conocer el largo de un string
print(len(n5))