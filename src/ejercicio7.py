#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
#El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
#Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

#Lista de la compra	
#Artículo 1	Precio
#Artículo 2	Precio
#Artículo 3	Precio

#Total	Coste

def imprimir_cesta_compra():
    cesta_compra = {}
    return cesta_compra

if __name__ == "__main__":
    cesta = imprimir_cesta_compra()
    articulo = input("Introduce el nombre del articulo (o 'fin' para terminar): ")

    while articulo.lower() != 'fin':
        precio = float(input("Introduce el precio del articulo: "))
        cesta[articulo] = precio
        articulo = input("Introduce el nombre del articulo (o 'fin' para terminar): ")

    print("Lista de la compra")
    total_coste = 0
    max_len = max(len(articulo) for articulo in cesta.keys())
    
    for articulo, precio in cesta.items():
        espacios = " " * (max_len - len(articulo))
        print(articulo + ":" + espacios + str(precio))
        total_coste += precio

    espacios_total = " " * (max_len - 5)
    print("Total:" + espacios_total + str(total_coste))
