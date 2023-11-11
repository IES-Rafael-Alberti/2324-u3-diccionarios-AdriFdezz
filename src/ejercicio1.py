#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario 
#por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def obtener_divisa(divisa):
    """
    Obtiene el símbolo de una divisa a partir de su nombre.

    Esta función toma el nombre de una divisa como entrada y devuelve el símbolo correspondiente.
    Si la divisa no está en el diccionario de divisas, se informa que no se encuentra en el diccionario.

    Args:
        divisa (str): El nombre de la divisa a consultar.

    Returns:
        str: Un mensaje que indica el símbolo de la divisa si se encuentra en el diccionario, o
             un mensaje de que la divisa no está en el diccionario.
    """
    divisas = {'euro': '€', 'dollar': '$', 'yen': '¥'}
    divisa = divisa.lower()
    if divisa in divisas:
        simbolo = divisas[divisa]
        return "El simbolo de " + divisa.capitalize() + " es " + simbolo
    else:
        return divisa.capitalize() + " no esta en el diccionario"

if __name__ == "__main__":
    divisa = input("Ingresa una divisa: ")
    resultado = obtener_divisa(divisa)
    print(resultado)

