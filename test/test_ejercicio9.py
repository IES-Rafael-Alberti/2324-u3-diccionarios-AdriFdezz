from src.ejercicio9 import gestionar_facturas

def test_gestionar_facturas():
        facturas = {}
        total_cobrado = 0
        opcion = "nueva"
        numero_factura = 1
        coste = 100

        mensaje, mensaje_cobrado, mensaje_pendiente = gestionar_facturas(facturas, total_cobrado, opcion, numero_factura, coste)

        assert mensaje == "Factura añadida.\n"
        assert mensaje_cobrado == "Cantidad cobrada hasta el momento: 0€"
        assert mensaje_pendiente == "Cantidad pendiente de cobro: 100€"
        assert facturas == {1: 100}
        assert total_cobrado == 0