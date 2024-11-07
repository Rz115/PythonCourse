x = 6
y = 2
z = 7
print(f"La suma de {x} y  {y} es igual a {x+y}")
print(f"La resta de {x} y  {y} es igual a {x-y}")
print(f"La multiplicación de {x} y  {y} es igual a {x*y}")
print(f"La divison de {x} y  {y} es igual a {x/y}")

#Division redondear cantidad pequeña a entero
print(f"{z} dividio al piso de {y} es igual a {z//y}")
#extraer residuo ó módulo de division
print(f"{z} modulo de {y} es igual a {z%y}")
#ELEVAR al cuadrado
print(f"{x} elevado a la  {y} es igual a {x**y}")
#ELEVAR al cubo
print(f"{x} elevado a la {3} es igual a {x**3}")
#Raiz Cuadrada
print(f"{x} La raiz cuadrada de {x} es igual a {x**0.5}")
#redondea y elimina muchos decimales
print(round(90/7))
#OTRA FORMA DE HACERLO
resultado = round(90/7)
print(resultado)
#imprimir la cantidad de decimales que yo quiero que redonde
print(round(95.666666666666666666, 3))
#Si se redondea fuera de la variable el tipo de dato
# siempre se va a respetar, aun que se redonde después
valor = 95.6666666666666666
print(round(valor))
print(type(valor))
#Si se redondea dentro de la variable el tipo de dato cambia y es ahora INT
valor = round(95.6666666666666666)
print(valor)
print(type(valor))

num1 = round(13/2,0)
print(num1)


d = 7
h = 10
print(d%h)