import speech_recognition as sr

# Crear un objeto de reconocimiento
recognizer = sr.Recognizer()

# Usar el micrófono para capturar el habla
with sr.Microphone() as source:
    print("Por favor, hable algo...")
    # Ajustar para el ruido ambiental
    recognizer.adjust_for_ambient_noise(source)
    # Escuchar la entrada de audio
    audio_data = recognizer.listen(source)
    print("Reconociendo...")

    try:
        # Reconocer el habla usando Google Web Speech API
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print(f"Usted dijo: {text}")
    except sr.UnknownValueError:
        print("Lo siento, no pude entender lo que dijo.")
    except sr.RequestError as e:
        print(f"Error al comunicarse con el servicio de reconocimiento: {e}")
"""
Importar Bibliotecas: Se importa la biblioteca speech_recognition para trabajar con el reconocimiento del habla.

Crear un Reconocedor: Se crea un objeto de la clase Recognizer, que es responsable del reconocimiento del habla.

Capturar Audio: Se utiliza el micrófono para capturar la entrada de audio. Se ajusta el reconocimiento para el ruido ambiental, se escucha la entrada y se guarda en audio_data.

Reconocimiento: Se usa el método recognize_google para convertir el audio en texto. Se especifica el idioma (español en este caso).

Manejo de Errores:

UnknownValueError: Se lanza si no se puede entender el habla.
RequestError: Se lanza si hay problemas de conexión con el servicio de reconocimiento.
"""