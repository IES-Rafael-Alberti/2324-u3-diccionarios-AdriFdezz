#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def agregar_informacion(informacion_persona, tipo_informacion, informacion):
    informacion_persona[tipo_informacion] = informacion

if __name__ == "__main__":
    informacion_persona = {}
    continuar = 's'
    
    while continuar.lower() == 's':
        tipo_informacion = input("Introduce la informacion (tipo de informacion que quieres almacenar): ")
        informacion = input("Introduce la informacion: ")
        agregar_informacion(informacion_persona, tipo_informacion, informacion)
        
        print("Informacion actual de la persona:")
        for tipo_informacion, informacion in informacion_persona.items():
            print(tipo_informacion, ":", informacion)
            
        continuar = input("¿Deseas agregar mas informacion? (s/n): ")
