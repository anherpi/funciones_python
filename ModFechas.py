from datetime import datetime, date
import locale
locale.setlocale(locale.LC_ALL, "es-ES") # Establecemos el idioma a Español


def calculaEdad(d, m, a):
    """ Función que calcula la edad a partir de la fecha de nacimiento.

    :param (int) d: Día de nacimiento.
    :param (int) m: Mes de nacimiento.
    :param (int) a: Año de nacimiento.
    :return: Tupla con dos valores enteros, la edad en años y la edad en días.
    :rtype tuple:
    """

    hoy = datetime.today()
    dia = int(d)
    mes = int(m)
    anyo = int(a)
    
    edad = hoy.year - anyo - ((hoy.month, hoy.day) < (mes, dia))
    dias_vividos = (datetime.today() - datetime(anyo, mes, dia)).days
    
    return edad, dias_vividos


def fechaActual():
    """
    Función que devuelve la fecha y hora actual

    :param: No tiene parámetros.
    :return: Tupla de strings con el día de la semana, día del mes, mes, año, hora, minuto y segundo actual.
    :rtype: tuple
    """

    dt = datetime.now()

    dia = str(dt.day).zfill(2)
    mes = str(dt.month).zfill(2)
    anyo = str(dt.year).zfill(2)
    hora = str(dt.hour).zfill(2)
    minuto = str(dt.minute).zfill(2)
    segundo = str(dt.second).zfill(2)

    hoy = datetime.today()
    diaSemana = hoy.strftime("%A")

    return diaSemana, dia, mes, anyo, hora, minuto, segundo


def diasEntreFechas(dia_inicio, mes_inicio, anyo_inicio, dia_final, mes_final, anyo_final):
    """
    Función que devuelve los días transcurridos entre dos fechas.

    :param (int) dia_inicio: Día de la fecha inicial.
    :param (int) mes_inicio: Mes de la fecha inicial:
    :param (int) anyo_inicio: Año de la fecha inicial.
    :param (int) dia_final: Día de la fecha final.
    :param (int) mes_final: Mes de la fecha final.
    :param (int) anyo_final: Año de la fecha final.
    :return: Días transcurridos entre las dos fechas.
    :rtype: int
    """

    fecha_inicio = date(anyo_inicio, mes_inicio, dia_inicio)
    fecha_fin = date(anyo_final, mes_final, dia_final)

    return (fecha_fin - fecha_inicio).days


if __name__ == "__main__":

    # EJEMPLO de la función: calculaEdad ----------------------------------------------------------

    anyos = calculaEdad(21, 5, 2000)[0]
    dias = calculaEdad(21, 5, 2000)[1]
    print("EJEMPLO de la función: calculaEdad")
    print("Si nacieste el 01/01/2000 tienes " + str(anyos) + " años (" + str(dias) + " días)")
    print("")

    # EJEMPLO de la función: fechaActual ----------------------------------------------------------

    print("EJEMPLO de la función: fechaActual")
    print("Fecha actual: " + fechaActual()[0] + " " + fechaActual()[1] + "/" + fechaActual()[2] + "/" + fechaActual()[3])
    print("Hora actual: " + fechaActual()[4] + ":" + fechaActual()[5] + ":" + fechaActual()[6])
    print("")

    # EJEMPLO de la función: diasEntreFechas ------------------------------------------------------
    print("EJEMPLO de la función: diasEntreFechas")
    print("Dias entre el 01/01/2000 y 23/05/2020:", diasEntreFechas(1, 1, 2000, 23, 5, 2020))
    print("")
