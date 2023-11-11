from src.ejercicio1 import obtener_divisa

def test_obtener_divisa():
        assert obtener_divisa('euro') == "El simbolo de Euro es €"
        assert obtener_divisa('dollar') == "El simbolo de Dollar es $"
        assert obtener_divisa('yen') == "El simbolo de Yen es ¥"