import win32com.client as wc
from googletrans import Translator


def textoAvoz(cadena, voz, volumen=100, velocidad=1):
    """ Función que reproduce un texto a voz.

    :param (str) cadena: Cadena de texto que queremos convertir a voz.
    :param (int) voz: 0 para texto en español, 1 para texto en inglés.
    :param (int) volumen: Volumen (valores de 0 a 100).
    :param (int) velocidad: '0' normal. Enteros negativos y positivos para más lento o más rápido.

    :return: Salida de voz del texto pasado como parámetro.
    :rtype: int
    """

    speak = wc.Dispatch("Sapi.SpVoice")
    speak.Voice = speak.GetVoices().item(voz)
    speak.Volume = volumen
    speak.Rate = velocidad
    print(speak.Speak(cadena))

    return speak.Speak(cadena)


def traducir(texto, idioma):
    """ Función que traduce un texto a otro idioma.

    :param (str) texto: Texto que queremos traducir.
    :param (str) idioma: Idioma al que queremos traducir ('en', 'ru', 'la'...).
    :return: Texto traducido.
    :rtype: str
    :nota: Para ver los lenguajes disponibles -> print(googletrans.LANGUAGES)
    """
    translator = Translator()
    traduccion = translator.translate(texto, dest=idioma)

    return traduccion.text


if __name__ == "__main__":

    # EJEMPLO de la función: textoAvoz ------------------------------------------------------------
    texto = "Esto es un texto de ejemplo."
    print("EJEMPLO de la función: textoAvoz\nReproduciendo...")
    textoAvoz(texto, 0, 100, 0)
    print("")

    # EJEMPLO de la función: traducir -------------------------------------------------------------
    print("EJEMPLO de la función: traducir")
    texto = 'Esto es un texto de ejemplo'
    print(texto, '(TRADUCCION)', traducir(texto, 'en'))
    print("")
