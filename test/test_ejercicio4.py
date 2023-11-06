from src.ejercicio4 import formato_fecha

def test_formato_fecha():
        assert formato_fecha("01/01/2023") == "01 de enero de 2023"