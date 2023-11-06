#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte 
#al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70

def calcular_precio_fruta(fruta, kilos):
    precios_frutas = {
        'platano': 1.35,
        'manzana': 0.80,
        'pera': 0.85,
        'naranja': 0.70
    }

    fruta = fruta.lower()

    if fruta in precios_frutas:
        precio_total = precios_frutas[fruta] * kilos
        return "El precio de " + str(kilos) + " kilos de " + fruta.capitalize() + " es: " + str(round(precio_total, 2)) + " euros"
    else:
        return fruta.capitalize() + " no esta en la lista de frutas disponibles."

if __name__ == "__main__":
    fruta = input("Ingresa el nombre de la fruta: ")
    kilos = float(input("Ingresa la cantidad de kilos: "))
    resultado = calcular_precio_fruta(fruta, kilos)
    print(resultado)

