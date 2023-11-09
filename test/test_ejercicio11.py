from src.ejercicio11 import procesar_directorio, crear_diccionario_cliente

def test_procesar_directorio():
    directorio_texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

    resultado = procesar_directorio(directorio_texto)

    assert '01234567L' in resultado
    assert '71476342J' in resultado
    assert '63823376M' in resultado
    assert '98376547F' in resultado

def test_crear_diccionario_cliente():
    campos = ['nif', 'nombre', 'email', 'teléfono', 'descuento']
    valores = ['01234567L', 'Luis González', 'luisgonzalez@mail.com', '656343576', '12.5']

    resultado = crear_diccionario_cliente(campos, valores)

    assert resultado['nif'] == '01234567L'
    assert resultado['nombre'] == 'Luis González'
    assert resultado['email'] == 'luisgonzalez@mail.com'
    assert resultado['teléfono'] == '656343576'
    assert resultado['descuento'] == 12.5