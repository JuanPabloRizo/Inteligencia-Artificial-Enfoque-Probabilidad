import numpy as np
from collections import defaultdict

class NGramModel:
    def __init__(self, n):
        self.n = n  # El valor de n para el modelo n-gram
        self.ngrams = defaultdict(int)  # Diccionario para contar n-gramas
        self.total_count = 0  # Contador total de n-gramas

    def train(self, text):
        # Preprocesar el texto (dividir en palabras)
        words = text.split()
        # Contar los n-gramas
        for i in range(len(words) - self.n + 1):
            ngram = tuple(words[i:i + self.n])
            self.ngrams[ngram] += 1
            self.total_count += 1

    def probability(self, ngram):
        # Calcula la probabilidad de un n-grama
        return self.ngrams[ngram] / self.total_count if self.total_count > 0 else 0

    def generate_sentence(self, starting_words, length=5):
        # Genera una oración basada en un n-grama dado
        current_ngram = tuple(starting_words.split())
        sentence = list(current_ngram)

        for _ in range(length):
            # Encuentra el siguiente n-grama
            possible_next_words = {ngram[-1] for ngram in self.ngrams if ngram[:-1] == current_ngram}
            if not possible_next_words:
                break
            next_word = np.random.choice(list(possible_next_words))
            sentence.append(next_word)
            current_ngram = tuple(sentence[-(self.n - 1):])  # Actualiza el n-grama actual

        return ' '.join(sentence)

# Ejemplo de uso
if __name__ == "__main__":
    # Texto de ejemplo para entrenar el modelo
    text = "El perro ladra. El gato maulla. El perro juega. El gato duerme."
    
    # Crea un modelo de bigramas
    bigram_model = NGramModel(n=2)
    # Entrena el modelo con el texto
    bigram_model.train(text)

    # Calcula la probabilidad de un bigrama
    bigram = ("El", "perro")
    print(f"Probabilidad de {bigram}: {bigram_model.probability(bigram)}")

    # Genera una oración a partir de palabras iniciales
    starting_words = "El perro"
    generated_sentence = bigram_model.generate_sentence(starting_words, length=5)
    print(f"Oración generada: {generated_sentence}")
"""
Clase NGramModel:

__init__: Inicializa el modelo con el valor de n y un diccionario para almacenar los n-gramas y su conteo.
train:
Preprocesa el texto dividiéndolo en palabras y cuenta los n-gramas.
Se usa un bucle para recorrer el texto y contar cuántas veces aparece cada n-grama.
probability:
Calcula la probabilidad de que un n-grama aparezca en el texto entrenado.
generate_sentence:
Genera una nueva oración basada en un conjunto de palabras iniciales. Utiliza el n-grama actual para predecir la siguiente palabra y la agrega a la oración.
Ejemplo de Uso:

Se entrena el modelo con un texto de ejemplo.
Se calcula la probabilidad de un bigrama específico.
Se genera una oración a partir de un conjunto de palabras iniciales.
"""