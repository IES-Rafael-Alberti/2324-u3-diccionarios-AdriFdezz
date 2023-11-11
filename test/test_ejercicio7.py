from src.ejercicio7 import imprimir_cesta_compra

def test_imprimir_cesta_compra():
        cesta_compra = imprimir_cesta_compra()
        cesta_compra['Platanos'] = 10
        cesta_compra['Manzanas'] = 5
    
        assert cesta_compra == {'Platanos': 10, 'Manzanas': 5}