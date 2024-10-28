import numpy as np

# Clase para la Red de Hopfield
class HopfieldNetwork:
    def __init__(self, num_neurons):
        # Inicializa el número de neuronas y los pesos de la red a cero
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        # Entrena la red utilizando patrones de entrada
        for pattern in patterns:
            # Convertir el patrón a un vector columna
            p = pattern.reshape(self.num_neurons, 1)
            # Actualiza los pesos utilizando la regla de Hebb
            self.weights += np.dot(p, p.T)
        # Pone a cero los pesos en la diagonal (sin retroalimentación)
        np.fill_diagonal(self.weights, 0)

    def predict(self, input_pattern, steps=5):
        # Preprocesar la entrada
        pattern = input_pattern.copy()
        for _ in range(steps):
            # Calcula la entrada neta
            net_input = np.dot(self.weights, pattern)
            # Aplica la función de activación binaria (1 si > 0, -1 si ≤ 0)
            pattern = np.where(net_input > 0, 1, -1)  
        return pattern  # Devuelve el patrón recuperado

# Clase para la Red de Boltzmann
class BoltzmannMachine:
    def __init__(self, num_visible, num_hidden):
        # Inicializa el número de neuronas visibles y ocultas
        self.num_visible = num_visible
        self.num_hidden = num_hidden
        # Inicializa los pesos aleatoriamente con una distribución normal
        self.weights = np.random.normal(0, 0.1, (num_visible, num_hidden))

    def sample_hidden(self, visible):
        # Calcula la probabilidad de activación de las neuronas ocultas
        hidden_probs = self.sigmoid(np.dot(visible, self.weights))
        # Devuelve una muestra aleatoria basada en las probabilidades
        return np.random.binomial(1, hidden_probs)

    def sample_visible(self, hidden):
        # Calcula la probabilidad de activación de las neuronas visibles
        visible_probs = self.sigmoid(np.dot(hidden, self.weights.T))
        # Devuelve una muestra aleatoria basada en las probabilidades
        return np.random.binomial(1, visible_probs)

    def train(self, data, num_epochs=1000):
        # Entrena la red utilizando un conjunto de datos
        for epoch in range(num_epochs):
            for sample in data:
                # Muestra las neuronas ocultas a partir de las visibles
                hidden = self.sample_hidden(sample)
                # Reconstruye las neuronas visibles a partir de las ocultas
                visible_reconstructed = self.sample_visible(hidden)
                # Aquí se puede implementar la actualización de pesos

    def sigmoid(self, x):
        # Función sigmoide para transformar las entradas
        return 1 / (1 + np.exp(-x))

# Ejemplo de uso
if __name__ == "__main__":
    # ------------------ Red de Hopfield ------------------
    # Define los patrones que se almacenarán en la red
    patterns = np.array([[1, 1, -1, -1],
                         [-1, -1, 1, 1]])
    
    # Crea una instancia de la red de Hopfield con 4 neuronas
    hopfield = HopfieldNetwork(num_neurons=4)
    # Entrena la red con los patrones
    hopfield.train(patterns)
    
    # Presenta un patrón ruidoso para la recuperación
    noisy_pattern = np.array([1, -1, -1, -1])
    
    # Predice el patrón almacenado utilizando el patrón ruidoso
    recovered_pattern = hopfield.predict(noisy_pattern)
    print("Patrón recuperado (Hopfield):", recovered_pattern)
    
    # ------------------ Red de Boltzmann ------------------
    # Genera datos binarios aleatorios para el entrenamiento
    data = np.random.randint(2, size=(100, 5))  # 100 muestras de 5 bits
    # Crea una instancia de la red de Boltzmann con 5 neuronas visibles y 3 ocultas
    boltzmann = BoltzmannMachine(num_visible=5, num_hidden=3)
    # Entrena la red con los datos generados
    boltzmann.train(data)
    
    # Genera un patrón visible a partir de un patrón oculto aleatorio
    hidden_sample = np.random.randint(2, size=3)  # 3 neuronas ocultas
    generated_visible = boltzmann.sample_visible(hidden_sample)
    print("Patrón generado (Boltzmann):", generated_visible)

"""
Clase HopfieldNetwork:
Inicialización: Se inicializan los pesos de la red a cero.
Método train: Entrena la red con patrones, actualizando los pesos en función de los patrones ingresados.
Método predict: Recupera un patrón a partir de una entrada parcial, usando la activación binaria.
Clase BoltzmannMachine:

Inicialización: Se definen el número de neuronas visibles y ocultas, y se inicializan los pesos aleatoriamente.
Métodos sample_hidden y sample_visible: Generan muestras de neuronas ocultas y visibles, respectivamente, utilizando la función sigmoide.
Método train: Entrena la red, aunque no se implementa la actualización de pesos en este ejemplo.
Ejemplo de Uso:

Se entrenan ambas redes con datos de muestra.
Se muestra el patrón recuperado de la red de Hopfield y un patrón generado por la red de Boltzmann.
"""