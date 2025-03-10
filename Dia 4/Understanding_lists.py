'''Comprension de listas, en este caso primero el ejemplo de lo que toma
el llenar una lista con el metodo arcaico '''
palabra = "python"
lista = []
for letra in palabra:
    lista.append(letra)

print(lista)

#Aplicando método de comprension de listas:
Lista = [letra for letra in "Python"]  #En una sola línea...
print(Lista)

#Aplicandolo tambien en integers:
Lista2 = [numero for numero in range(0,21,2)]
print(Lista2)

#Incluso puedes alterar la variable antes de incluírlo dentro de la lista:
Lista2 = [(numero * 2) for numero in range(0,21,2)] #Yo agregué el parentesis para mayor legibilidad, pero funciona sin el
print(Lista2)

#Incluso puedes incluir condicionales:
Lista2 = [numero for numero in range(0,21,2) if numero * 2 > 10]
print(Lista2)

#Al momento de incluir else ya la condicional pasa al inicio para que se lea así:
Lista2 = [numero if numero * 2 > 10 else "No" for numero in range(0,21,2)]
print(Lista2)

#Otro ejemplo más real:
pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)

#Section test 1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]
print(valores_cuadrado)

#Section test 2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [numero for numero in valores if numero%2 == 0]
print(valores_pares)

#Sectiont test 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados_farenheit-32)*(5/9) for grados_farenheit in temperatura_fahrenheit]
print(grados_celsius)

