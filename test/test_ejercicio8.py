from src.ejercicio8 import traducir_frase

def test_traducir_frase():
        diccionario = {"hola": "hello", "mundo": "world"}
        frase = "hola mundo"
        assert traducir_frase(diccionario, frase) == "hello world"