precios_cafe = [('Makiato', 1.20), ('Expresso', 2.5), ('Mokachino', 2.1)]


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass

    return cafe_caro, precio_mayor


cafek, precioek = cafe_mas_caro(precios_cafe)
print(f"El cafe más caro es {cafek} y su precio es de {precioek}.")