#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario 
#por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def obtener_divisa(divisa):
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

