import locale
import random


def puntoDeMiles(numero, decimales):
    """
    Función que formatea un número con decimales y punto de miles.

    :param (int) numero: Número a representar.
    :param (int) decimales: Cantidad de decimales que se van a representar.
    :return: Número formateado con puntos de miles y decimales especificados.
    :rtype str
    """

    locale.setlocale(locale.LC_ALL, "es-ES.utf-8")
    formato = '%.' + str(decimales) + 'f'

    return locale.format_string(formato, numero, 1)


def generaAleatorios(n, desde, hasta):
    """
    Función que obtiene una lista ordenada de n números aleatorios entre un rango de números.

    :param (int) n: Número de elementos que queremos obtener.
    :param (int) desde: Inicio del rango de números sobre el que se obtendrán los aleatorios.
    :param (int) hasta: Fin del rango de números sobre el que se obtendrán los aleatorios.
    :return: Lista ordenada con los 'n' números aleatorios.
    :rtype: list
    :
    """

    hasta += 1
    elementos = []
    numerosObtenidos = 0

    while numerosObtenidos < n:
        numero = random.randrange(desde, hasta)

        if numero not in elementos:
            elementos.append(numero)
            numerosObtenidos += 1

    elementos.sort()

    return elementos


if __name__ == "__main__":

    # EJEMPLO de la función: puntoDeMiles ---------------------------------------------------------
    print("")
    print("EJEMPLO de la función: puntoDeMiles")
    numero = 1234567.891
    print("Formateo del número 1234567,891:", puntoDeMiles(numero, 2))
    print("")

    # EJEMPLO de la función: generaAleatorios -----------------------------------------------------
    print("EJEMPLO de la función: generaAleatorios")
    print("6 números aleatorios entre 1 y 49 sin repetición:", generaAleatorios(6, 1, 49))
    print("")
