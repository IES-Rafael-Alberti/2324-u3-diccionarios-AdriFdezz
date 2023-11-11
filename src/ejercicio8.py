#Escribir un programa que cree un diccionario de traducción español-inglés. 
#El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.
#El programa debe crear un diccionario con las palabras y sus traducciones. 
#Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
#Si una palabra no está en el diccionario debe dejarla sin traducir.

def traducir_frase(diccionario, frase):
    """
    Traduce una frase de español a inglés utilizando un diccionario de traducción.

    Esta función toma un diccionario de traducción y una frase en español. Divide la frase en palabras,
    busca cada palabra en el diccionario y la traduce al inglés. Si una palabra no está en el diccionario,
    se mantiene sin cambios en la frase traducida.

    Args:
        diccionario (dict): Un diccionario que mapea palabras en español a sus traducciones en inglés.
        frase (str): La frase en español que se desea traducir.

    Returns:
        str: La frase traducida al inglés, donde las palabras traducidas se sustituyen y las no traducidas se mantienen igual.
    """
    palabras = frase.split()
    frase_traducida = []

    for palabra in palabras:
        traduccion = diccionario.get(palabra, palabra)
        frase_traducida.append(traduccion)

    return " ".join(frase_traducida)

if __name__ == "__main__":
    diccionario = {}
    entrada = input("Introduce las palabras en español e inglés (ejemplo: palabra:word, otra:another): ")

    pares = entrada.split(",")

    for par in pares:
        palabra, traduccion = par.strip().split(":")
        diccionario[palabra.strip()] = traduccion.strip()

    frase_espanol = input("Introduce una frase en español: ")
    frase_traducida = traducir_frase(diccionario, frase_espanol)
    print("Frase traducida al ingles:", frase_traducida)
