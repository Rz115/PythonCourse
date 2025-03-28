def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


'''Estos dos son un args y un kwargs solo con el nombre cambiado, además se invocan
en la funcion prueba hasta abajo con sus respectivos asteriscos...'''

valores = [10, 20, 30, 40, 50]
valoresextra = {'x': 'uno', 'y': 'dos', 'z': 'tres'}

prueba(15, 50, *valores, **valoresextra)

