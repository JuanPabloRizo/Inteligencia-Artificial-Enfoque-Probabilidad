# Diccionario de traducción
# Este diccionario contiene las traducciones de palabras del español al inglés.
# Cada clave es una palabra en español y el valor asociado es su traducción en inglés.
translation_dict = {
    'hola': 'hello',       # 'hola' se traduce como 'hello'
    'mundo': 'world',      # 'mundo' se traduce como 'world'
    'como': 'how',         # 'como' se traduce como 'how'
    'estas': 'are you',    # 'estas' se traduce como 'are you'
    'bien': 'well'         # 'bien' se traduce como 'well'
}

# Función para traducir una frase
def translate(sentence):
    # La función 'translate' toma una oración como argumento y devuelve la oración traducida.
    
    # Dividir la frase en palabras usando el método split(). Esto convierte la oración en una lista de palabras.
    words = sentence.split()  
    translated_words = []  # Inicializa una lista vacía para almacenar las palabras traducidas.
    
    # Traducir cada palabra
    for word in words:  # Itera a través de cada palabra en la lista 'words'.
        # Remover signos de puntuación de la palabra
        # strip() elimina los signos de puntuación especificados en la cadena.
        cleaned_word = word.strip(",.!?")  
        
        # Traducir la palabra usando el diccionario.
        # Si la palabra está en el diccionario, se traduce; de lo contrario, se mantiene igual.
        translated_word = translation_dict.get(cleaned_word, cleaned_word)
        
        # Agrega la palabra traducida a la lista 'translated_words'.
        translated_words.append(translated_word)  
    
    # Unir las palabras traducidas en una frase usando join().
    return " ".join(translated_words)  

# Frase a traducir
# Aquí se define la oración en español que se quiere traducir.
input_sentence = "hola mundo, como estas bien"

# Realizar la traducción
# Se llama a la función 'translate' con la frase de entrada y se guarda el resultado en 'translated_sentence'.
translated_sentence = translate(input_sentence)  

# Mostrar resultados
# Se imprime la frase original y la traducida.
print(f"Frase original: {input_sentence}")
print(f"Frase traducida: {translated_sentence}")
"""
Diccionario de Traducción: Se define un diccionario translation_dict que mapea palabras en español a sus traducciones en inglés.

Función de Traducción: La función translate toma una oración como entrada, la divide en palabras y traduce cada palabra utilizando el diccionario. Si una palabra no se encuentra en el diccionario, se mantiene sin cambios.

Uso de la Función: Se define una oración de entrada y se llama a la función de traducción, imprimiendo tanto la oración original como la traducida.
"""