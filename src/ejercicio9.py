#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
#Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
#El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
#Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
#Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
#Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

def gestionar_facturas(facturas, total_cobrado, opcion, numero_factura, coste):
    mensaje = ""

    if opcion == "nueva":
        facturas[numero_factura] = coste
        mensaje = "Factura añadida.\n"

    elif opcion == "pagar":
        if numero_factura in facturas:
            total_cobrado += facturas[numero_factura]
            del facturas[numero_factura]
            mensaje = "Factura pagada."
        else:
            mensaje = "La factura no existe."

    cantidad_pendiente = sum(facturas.values())
    mensaje_cobrado = "Cantidad cobrada hasta el momento: " + str(total_cobrado) + "€"
    mensaje_pendiente = "Cantidad pendiente de cobro: " + str(cantidad_pendiente) + "€"

    return mensaje, mensaje_cobrado, mensaje_pendiente

if __name__ == "__main__":
    facturas = {}
    total_cobrado = 0
    opcion = None

    while opcion != "fin":
        print("")
        print("-----------------------------------------------------")
        print("Gestion de Facturas")
        print("nueva - Añadir nueva factura")
        print("pagar - Pagar factura existente")
        print("fin - Terminar programa")
        print("-----------------------------------------------------")
        opcion = input("Selecciona una opcion (nueva/pagar/fin): ")

        if opcion == "nueva":
            numero_factura = input("Introduce el numero de factura: ")
            coste = float(input("Introduce el coste de la factura: "))
        elif opcion == "pagar":
            numero_factura = input("Introduce el numero de factura a pagar: ")

        mensaje, mensaje_cobrado, mensaje_pendiente = gestionar_facturas(facturas, total_cobrado, opcion, numero_factura, coste)
        print(mensaje)
        print(mensaje_cobrado)
        print(mensaje_pendiente)
