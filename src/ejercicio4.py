#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
#la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def formato_fecha(fecha_str):
    partes = fecha_str.split('/')

    if len(partes) == 3:
        dia, mes, anio = partes

        meses = {
            '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
            '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
            '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
        }

        if mes in meses:
            nombre_mes = meses[mes]
            fecha_formateada = dia + " de " + nombre_mes + " de " + anio
            return fecha_formateada

    return "Fecha no válida"

if __name__ == "__main__":
    fecha_str = input("Ingresa la fecha en formato dd/mm/aaaa: ")
    fecha_formateada = formato_fecha(fecha_str)
    print(fecha_formateada)
