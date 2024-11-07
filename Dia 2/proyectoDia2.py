nombre = input("Dime tu nombre: ")
#Conviertes el string a integer en la misma entrada de dato
mensualidad = int(input("Cuánto haz vendido este mes: "))
#imprimes sin importar formato y rendondeas el resultado a la vez que haces una operacion para sacar 13% del total
print(f"Tu nombre es {nombre} y tu comision es de $ {round(mensualidad*0.13,2)}")