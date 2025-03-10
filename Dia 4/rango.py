''' rango de datos el primero marca desde donde, el segundo el limite pero sin incluir ese
numero y el tercero para elegir cada cuántos pasos o numeros avanza hasta entregar
el resultado, RANGE no recibe floats'''
for letra in range(10,51,2):
    print(letra)

#Tambien se puede usar casting:
lista = list(range(1,101,2))
print(lista)

#Small test
suma_cuadrados = 0
suma_de_elemento_al_cuadrado = 0
for elemento in range(1,16):
    elemento_al_cuadrado = elemento**2
    suma_de_elemento_al_cuadrado += elemento_al_cuadrado
    suma_cuadrados = suma_de_elemento_al_cuadrado
    print(suma_cuadrados)