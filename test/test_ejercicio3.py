from src.ejercicio3 import calcular_precio_fruta

def test_calcular_precio_fruta():
        assert calcular_precio_fruta('platano', 2) == "El precio de 2 kilos de Platano es: 2.7 euros"
        assert calcular_precio_fruta('manzana', 1.5) == "El precio de 1.5 kilos de Manzana es: 1.2 euros"
        assert calcular_precio_fruta('pera', 3) == "El precio de 3 kilos de Pera es: 2.55 euros"
        assert calcular_precio_fruta('naranja', 0.5) == "El precio de 0.5 kilos de Naranja es: 0.35 euros"