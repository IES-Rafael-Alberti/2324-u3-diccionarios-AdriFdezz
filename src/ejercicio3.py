#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte 
#al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70

def calcular_precio_fruta(fruta, kilos):
    """
    Calcula el precio de una cantidad de fruta en función de su tipo y peso.

    Esta función toma el nombre de una fruta y la cantidad en kilos como entrada
    y calcula el precio total en euros de la fruta en base a su tipo y cantidad.

    Args:
        fruta (str): El nombre de la fruta a calcular el precio.
        kilos (float): La cantidad en kilos de la fruta.

    Returns:
        str: Un mensaje que indica el precio de la fruta en euros si se encuentra en la lista de frutas disponibles,
             o un mensaje que informa que la fruta no está en la lista de frutas disponibles.
    """
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

