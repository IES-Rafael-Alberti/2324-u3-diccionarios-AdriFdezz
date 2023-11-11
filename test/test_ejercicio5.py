from src.ejercicio5 import mostrar_creditos

def test_mostrar_creditos():
    creditos_asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
    total_creditos = mostrar_creditos(creditos_asignaturas)
    assert total_creditos == 15