from src.ejercicio6 import agregar_informacion

def test_agregar_informacion_persona():
    informacion_persona = {}
    tipo_informacion = "nombre"
    informacion = "Juan"
    agregar_informacion(informacion_persona, tipo_informacion, informacion)
    
    assert informacion_persona == {"nombre": "Juan"}