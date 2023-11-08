#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos 
#de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
#Al final debe mostrar también el número total de créditos del curso.

def mostrar_creditos(creditos_asignaturas):
    total_creditos = sum(creditos_asignaturas.values())
    return total_creditos

if __name__ == "__main__":
    creditos_asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
    total_creditos = mostrar_creditos(creditos_asignaturas)

    for asignatura, creditos in creditos_asignaturas.items():
        print(asignatura + " tiene " + str(creditos) + " creditos")

    print("El numero total de creditos del curso es: " + str(total_creditos))
