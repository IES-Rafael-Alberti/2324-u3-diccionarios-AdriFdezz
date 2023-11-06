#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def informacion_usuario(nombre, edad, direccion, telefono):
    usuario = {
        'nombre': nombre,
        'edad': edad,
        'direccion': direccion,
        'telefono': telefono
    }

    mensaje = usuario['nombre'] + ' tiene ' + usuario['edad'] + ' años, vive en ' + usuario['direccion'] + ' y su numero de telefono es ' + usuario['telefono'] + '.'
    return mensaje

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    direccion = input("Ingresa tu direccion: ")
    telefono = input("Ingresa tu número de telefono: ")

    resultado = informacion_usuario(nombre, edad, direccion, telefono)
    print(resultado)
