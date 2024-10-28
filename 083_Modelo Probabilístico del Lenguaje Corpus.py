import numpy as np  # Importa NumPy, aunque no se usa directamente en este código.
import random  # Importa la librería random para generar selecciones aleatorias.
from collections import defaultdict  # Importa defaultdict para crear diccionarios con valores predeterminados.

class NGramModel:
    def __init__(self, n):
        """
        Inicializa el modelo n-grama.
        
        :param n: El tamaño del n-grama (2 para bigramas).
        """
        self.n = n  # Guarda el valor de n.
        # Crea un diccionario anidado para almacenar los n-gramas y sus conteos.
        self.ngrams = defaultdict(lambda: defaultdict(int))  
        # Crea un diccionario para almacenar el conteo de cada contexto.
        self.context_counts = defaultdict(int)  

    def train(self, corpus):
        """
        Entrena el modelo utilizando el corpus proporcionado.
        
        :param corpus: Un string que contiene el texto para el entrenamiento.
        """
        # Tokeniza el corpus en palabras utilizando el espacio como separador.
        words = corpus.split()  
        
        # Recorre las palabras en el corpus hasta la penúltima.
        for i in range(len(words) - 1):
            # Incrementa el conteo del bigrama (palabra actual, siguiente palabra).
            self.ngrams[words[i]][words[i + 1]] += 1  
            # Incrementa el conteo del contexto de la palabra actual.
            self.context_counts[words[i]] += 1  

    def bigram_probability(self, word1, word2):
        """
        Calcula la probabilidad de que word2 siga a word1.
        
        :param word1: La primera palabra del bigrama.
        :param word2: La segunda palabra del bigrama.
        :return: Probabilidad de (word1, word2).
        """
        # Si el contexto de word1 no tiene conteos, devuelve 0.0 para evitar división por cero.
        if self.context_counts[word1] == 0:
            return 0.0  
        
        # Calcula la probabilidad dividiendo el conteo del bigrama por el conteo del contexto.
        return self.ngrams[word1][word2] / self.context_counts[word1]  

    def generate_sentence(self, start_word, length):
        """
        Genera una oración a partir de una palabra inicial.
        
        :param start_word: La palabra inicial para la oración.
        :param length: La longitud deseada de la oración.
        :return: Una cadena que representa la oración generada.
        """
        current_word = start_word  # Inicializa la palabra actual con la palabra de inicio.
        sentence = [current_word]  # Crea una lista para almacenar las palabras de la oración.

        # Repite el proceso para la longitud deseada menos uno (ya que la palabra inicial ya se cuenta).
        for _ in range(length - 1):
            # Obtiene las palabras siguientes posibles para la palabra actual.
            next_words = list(self.ngrams[current_word].keys())  
            
            # Si no hay palabras siguientes posibles, se termina la generación.
            if not next_words:
                break  

            # Obtiene los conteos de las palabras siguientes para calcular las probabilidades.
            probabilities = [self.ngrams[current_word][word] for word in next_words]  
            total = sum(probabilities)  # Suma los conteos para normalizar las probabilidades.
            probabilities = [p / total for p in probabilities]  # Normaliza las probabilidades.

            # Selecciona aleatoriamente la siguiente palabra basada en las probabilidades.
            current_word = random.choices(next_words, weights=probabilities)[0]  
            sentence.append(current_word)  # Agrega la palabra seleccionada a la oración.

        return ' '.join(sentence)  # Une las palabras en la lista y devuelve la oración como un string.

# Ejemplo de uso
corpus = "El perro juega. El gato duerme. El perro ladra. El gato juega."  # Definimos un corpus de ejemplo.
model = NGramModel(n=2)  # Crea una instancia del modelo n-grama para bigramas.
model.train(corpus)  # Entrena el modelo usando el corpus proporcionado.

# Calcular la probabilidad de un bigrama
prob = model.bigram_probability("El", "perro")  # Calcula la probabilidad del bigrama ('El', 'perro').
print(f"Probabilidad de ('El', 'perro'): {prob:.2f}")  # Imprime la probabilidad.

# Generar una oración a partir de una palabra inicial
generated_sentence = model.generate_sentence("El", 5)  # Genera una oración comenzando con 'El' de longitud 5.
print(f"Oración generada: {generated_sentence}")  # Imprime la oración generada.
"""
Clase NGramModel: Define un modelo n-grama, donde n es el número de palabras en la secuencia (en este caso, 2 para bigramas).

self.ngrams: Almacena los recuentos de bigramas en un diccionario anidado.
self.context_counts: Almacena el número total de ocurrencias de cada palabra como contexto.
Método train: Toma un corpus de texto y cuenta los bigramas, actualizando self.ngrams y self.context_counts.

Método bigram_probability: Calcula la probabilidad de que una palabra siga a otra utilizando los recuentos de bigramas.

Método generate_sentence: Genera una oración comenzando con una palabra inicial y continuando con palabras que siguen a la anterior según las probabilidades de los bigramas.

Ejemplo de uso:

Se entrena el modelo con un pequeño corpus de ejemplo.
Se calcula la probabilidad del bigrama ("El", "perro").
Se genera una oración a partir de la palabra inicial "El".
"""