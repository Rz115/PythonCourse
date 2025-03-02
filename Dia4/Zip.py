'''Llega hasta el largo de la lista más corta, por eso aun que agreguemos
más valores a solo una lista va a omitir todos los valores restantes, es decir
si en lista 1 tenemos 3 valores y en lista 2 tenemos 6 valores, solo los primeros
3 valores de lista 2 podrán ser mostrados como se ve a continuación'''
nombres = ['Raul','Sergio','Alan']
edades = [27,30,100,55,23]
ciudades = ['mexico','lima','Madrid','chile']

combinarlos = list(zip(nombres,edades,ciudades))
print(combinarlos)

'''Pueden ser dos o más listas las que se puedan combinar, así tendríamos 
una lista de tuples...'''

for nombres,edades,ciudades in combinarlos:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}")

#Section test 1:
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
colleciones = list(zip(paises,capitales))
for paises,capitales in colleciones:
    print(f"La capital de {paises} es {capitales}")

#Section test 2:
marcas = ['nikedinero','addidas','destroya']
productos = ['playeras','tennis','mcr','chicharos']
mi_zip = zip(marcas,productos)
print(mi_zip) ; '''falta casteo aqui ya que como tal se combinan las listas pero 
solo son un objeto que necesita convertirse en tipo de dato '''

#Section test 3:
espanol = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']
numeros = list(zip(espanol,portugues,ingles))
print(numeros)
