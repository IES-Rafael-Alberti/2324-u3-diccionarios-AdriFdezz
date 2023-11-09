#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
#Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario 
#con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True 
#si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
#(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, 
#(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.

def mostrar_cliente(cliente):
    """
    Muestra los detalles de un cliente.

    Args:
        cliente (dict): Un diccionario que contiene los datos del cliente.

    Returns:
        str: Un mensaje formateado con los datos del cliente.
    """
    mensaje = []
    mensaje.append("NIF: " + cliente['NIF'])
    mensaje.append("Nombre: " + cliente['nombre'])
    mensaje.append("Direccion: " + cliente['direccion'])
    mensaje.append("Telefono: " + cliente['telefono'])
    mensaje.append("Correo: " + cliente['correo'])
    if cliente['preferente']:
        mensaje.append("Cliente Preferente")
    return '\n'.join(mensaje)

def listar_clientes(clientes):
    """
    Lista todos los clientes.

    Args:
        clientes (dict): Un diccionario que contiene a todos los clientes.

    Returns:
        list: Una lista de mensajes formateados con los datos de todos los clientes.
    """
    lista_clientes = []
    for nif, cliente in clientes.items():
        lista_clientes.append("NIF: " + nif)
        lista_clientes.append("Nombre: " + cliente['nombre'])
        lista_clientes.append("")
    return lista_clientes

def listar_clientes_preferentes(clientes):
    """
    Lista los clientes preferentes.

    Args:
        clientes (dict): Un diccionario que contiene a todos los clientes.

    Returns:
        list: Una lista de mensajes formateados con los datos de los clientes preferentes.
    """
    lista_preferentes = []
    for nif, cliente in clientes.items():
        if cliente['preferente']:
            lista_preferentes.append("NIF: " + nif)
            lista_preferentes.append("Nombre: " + cliente['nombre'])
            lista_preferentes.append("")
    return lista_preferentes

def añadir_cliente(clientes, nif, nombre, dirección, teléfono, correo, preferente):
    """
    Añade un cliente a la base de datos.

    Args:
        clientes (dict): Un diccionario que contiene a todos los clientes.
        nif (str): El NIF del cliente.
        nombre (str): El nombre del cliente.
        dirección (str): La direccion del cliente.
        teléfono (str): El telefono del cliente.
        correo (str): El correo del cliente.
        preferente (bool): True si el cliente es preferente, False en caso contrario.

    Returns:
        str: Un mensaje que indica si el cliente fue añadido correctamente.
    """
    cliente = {
        'NIF': nif,
        'nombre': nombre,
        'direccion': dirección,
        'telefono': teléfono,
        'correo': correo,
        'preferente': preferente
    }
    clientes[nif] = cliente
    return "Cliente añadido."

def eliminar_cliente(clientes, nif):
    """
    Elimina un cliente de la base de datos.

    Args:
        clientes (dict): Un diccionario que contiene a todos los clientes.
        nif (str): El NIF del cliente a eliminar.

    Returns:
        str: Un mensaje que indica si el cliente fue eliminado o si no existe.
    """
    if nif in clientes:
        del clientes[nif]
        return "Cliente eliminado."
    else:
        return "El cliente no existe."

def menu():
    """
    Función principal que muestra el menu de opciones y gestiona las operaciones con los clientes.
    """
    clientes = {}
    opcion = None

    while opcion != "6":
        print("-------------------------------------------")
        print("Menu de Clientes")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")
        print("-------------------------------------------")

        opcion = input("Selecciona una opcion (1/2/3/4/5/6): ")

        if opcion == "1":
            nif = input("Introduce el NIF del cliente: ")
            nombre = input("Introduce el nombre del cliente: ")
            dirección = input("Introduce la direccion del cliente: ")
            teléfono = input("Introduce el telefono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            preferente = input("¿Es un cliente preferente? (Si/No): ").lower() == "si"
            mensaje = añadir_cliente(clientes, nif, nombre, dirección, teléfono, correo, preferente)
            print(mensaje)

        elif opcion == "2":
            nif = input("Introduce el NIF del cliente a eliminar: ")
            mensaje = eliminar_cliente(clientes, nif)
            print(mensaje)

        elif opcion == "3":
            nif = input("Introduce el NIF del cliente a mostrar: ")
            if nif in clientes:
                cliente = clientes[nif]
                mensaje = mostrar_cliente(cliente)
                print(mensaje)
            else:
                print("El cliente no existe.")

        elif opcion == "4":
            clientes_lista = listar_clientes(clientes)
            for cliente in clientes_lista:
                print(cliente)

        elif opcion == "5":
            preferentes_lista = listar_clientes_preferentes(clientes)
            for preferente in preferentes_lista:
                print(preferente)

if __name__ == "__main__":
    menu()