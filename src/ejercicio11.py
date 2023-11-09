#El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene 
#la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
#Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información 
#contenida en el directorio.

#"nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

#Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento 
#corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. 
#Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores 
#la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

#{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}

def procesar_directorio(directorio_texto):
    """
    Procesa una cadena de texto que contiene informacion de un directorio de clientes y devuelve un diccionario con la informacion.

    Args:
        directorio_texto (str): La cadena de texto que contiene la informacion del directorio.

    Returns:
        dict: Un diccionario donde cada elemento corresponde a un cliente con el NIF como clave y un diccionario con el resto de la informacion como valor.
    """
    lineas = directorio_texto.split('\n')
    campos = lineas[0].split(';')
    directorio = {}
    for linea in lineas[1:]:
        valores = linea.split(';')
        cliente_info = crear_diccionario_cliente(campos, valores)
        directorio[valores[0]] = cliente_info
    return directorio

def crear_diccionario_cliente(campos, valores):
    """
    Crea un diccionario con la informacion de un cliente a partir de los campos y valores.

    Args:
        campos (list): Una lista de los nombres de los campos.
        valores (list): Una lista de los valores correspondientes al cliente.

    Returns:
        dict: Un diccionario con la informacion del cliente.
    """
    cliente_info = {}
    for i in range(len(campos)):
        campo = campos[i]
        valor = valores[i]
        if campo == 'descuento':
            valor = float(valor)
        cliente_info[campo] = valor
    return cliente_info

if __name__ == "__main__":
    directorio_texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    directorio = procesar_directorio(directorio_texto)
    print(directorio)
