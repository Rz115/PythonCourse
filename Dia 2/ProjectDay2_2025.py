#Empresa DevectorCorp - Vendedores reciben comisiones del 13% por
#sus ventas totales, calcular comisiones..
nombre = input("Hola, por favor introducte tu nombre: " )
ingreso_mes = input("Hola, ¿cuánto haz vendido este mes?: $")
print(f"Estimado/a {nombre} tu comisión de este mes es de: ${round(float(ingreso_mes)*0.13,2)}")