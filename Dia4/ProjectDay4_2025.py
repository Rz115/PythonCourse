'''El programa le debe pedir al usuario su nombre y luego debe decirle al usuario
 que adivine el numero que está pensando del 1 al 100 y que el usuario solo tiene 8 intentos
 en cada intento debe haber 4 maneras de responder:
 1.-Si el numero elegido por el usuario es menor a 1 ó superior a 100 - Numero no permitido
 2.- si el numero es menor a lo que ha pensado el programa - Respuesta incorrecta, haz seleccionado un
 numero menor... intenta de nuevo solo si quedan oportunidades.
 3.- Si el numero es mayor a lo que ha pensado el programa - Respuesta incorrecta, haz seleccionado un
 numero mayor... intenta de nuevo solo si quedan oportunidades
 4.- Si el usuario acierta se le dirá informará que ha ganado y cuántos intentos le ha tomado.
 '''

from random import *

aleatorio = randint(1, 100)
#print(aleatorio)
print("¡Bienvenido!")
nombre = input("\nPor favor introduce tu nombre: ")
for intentos in range(1, 9):
    numero_usuario = input("Por favor introduce un numero entre 1 y 100 para adivinar el numero secreto: ")
    transformar = int(numero_usuario)
    if intentos <= 8 and transformar > 100 or transformar < 1:
        print("¡NUMERO NO PERMITIDO!, solo insertar numeros del 1 al 100")
    elif intentos < 8 and aleatorio < transformar:
        print("¡Incorrecto!, el numero secreto es menor, intenta de nuevo")
        intentos += 1
    elif intentos < 8 and aleatorio > transformar:
        print("¡Incorrecto!, el numero secreto es mayor, intenta de nuevo")
        intentos += 1
    elif intentos < 8 and aleatorio == transformar:
        print(f"\n¡Correcto!, ganaste {nombre} y te llevo {intentos} intentos")
        break
    elif intentos == 8 and aleatorio != transformar:
        print(f"\n¡Perdiste {nombre}!, no lograste adivinar en {intentos} intentos...")
        break



