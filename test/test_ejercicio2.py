from src.ejercicio2 import informacion_usuario

def test_informacion_usuario():
    nombre = "Adrian"
    edad = "22"
    direccion = "Calle Arboleda n5"
    telefono = "1234567890"

    resultado = informacion_usuario(nombre, edad, direccion, telefono)

    assert resultado == "Adrian tiene 22 años, vive en Calle Arboleda n5 y su numero de telefono es 1234567890."