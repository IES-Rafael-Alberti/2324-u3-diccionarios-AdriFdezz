from src.ejercicio10 import añadir_cliente, eliminar_cliente, mostrar_cliente, listar_clientes, listar_clientes_preferentes

def test_añadir_cliente():
    clientes = {}
    mensaje = añadir_cliente(clientes, "12345678A", "Cliente1", "Direccion1", "123456789", "correo1@gmail.com", True)
    assert mensaje == "Cliente añadido."
    assert "12345678A" in clientes

def test_eliminar_cliente():
    clientes = {"12345678A": {
        'NIF': "12345678A",
        'nombre': "Cliente1",
        'direccion': "Dirección1",
        'telefono': "123456789",
        'correo': "correo1@gmail.com",
        'preferente': True
    }}
    mensaje = eliminar_cliente(clientes, "12345678A")
    assert mensaje == "Cliente eliminado."
    assert "12345678A" not in clientes

def test_mostrar_cliente():
    cliente = {
        'NIF': "12345678A",
        'nombre': "Cliente1",
        'direccion': "Direccion1",
        'telefono': "123456789",
        'correo': "correo1@gmail.com",
        'preferente': True
    }
    mensaje = mostrar_cliente(cliente)
    assert "NIF: 12345678A" in mensaje
    assert "Nombre: Cliente1" in mensaje
    assert "Direccion: Direccion1" in mensaje
    assert "Telefono: 123456789" in mensaje
    assert "Correo: correo1@gmail.com" in mensaje
    assert "Cliente Preferente" in mensaje

def test_listar_clientes():
    clientes = {
        "12345678A": {
            'NIF': "12345678A",
            'nombre': "Cliente1",
            'direccion': "Direccion1",
            'telefono': "123456789",
            'correo': "correo1@gmail.com",
            'preferente': True
        },
        "87654321B": {
            'NIF': "87654321B",
            'nombre': "Cliente2",
            'direccion': "Dirección2",
            'telefono': "987654321",
            'correo': "correo2@gmail.com",
            'preferente': False
        }
    }
    lista = listar_clientes(clientes)
    assert "NIF: 12345678A" in lista
    assert "Nombre: Cliente1" in lista
    assert "NIF: 87654321B" in lista
    assert "Nombre: Cliente2" in lista

def test_listar_clientes_preferentes():
    clientes = {
        "12345678A": {
            'NIF': "12345678A",
            'nombre': "Cliente1",
            'direccion': "Direccion1",
            'telefono': "123456789",
            'correo': "correo1@gmail.com",
            'preferente': True
        },
        "87654321B": {
            'NIF': "87654321B",
            'nombre': "Cliente2",
            'direccion': "Direccion2",
            'telefono': "987654321",
            'correo': "correo2@gmail.com",
            'preferente': False
        }
    }
    preferentes = listar_clientes_preferentes(clientes)
    assert "NIF: 12345678A" in preferentes
    assert "Nombre: Cliente1" in preferentes
    assert "NIF: 87654321B" not in preferentes
    assert "Nombre: Cliente2" not in preferentes