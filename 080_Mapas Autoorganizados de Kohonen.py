import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia euclidiana
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

# Función para la actualización de pesos
def update_weights(weights, input_vector, learning_rate):
    return weights + learning_rate * (input_vector - weights)

# Parámetros del mapa
num_neurons = (10, 10)  # 10x10 neuronas
num_iterations = 100  # Número de iteraciones
learning_rate_initial = 0.5  # Tasa de aprendizaje inicial
decay = 0.05  # Decaimiento de la tasa de aprendizaje

# Inicialización del mapa de pesos
weights = np.random.rand(num_neurons[0], num_neurons[1], 2)  # 2D para datos 2D

# Generación de datos de entrada aleatorios (ejemplo)
data = np.random.rand(100, 2)  # 100 puntos en 2D

# Entrenamiento del mapa
for iteration in range(num_iterations):
    learning_rate = learning_rate_initial * np.exp(-decay * iteration)  # Decaimiento de la tasa de aprendizaje
    for input_vector in data:
        # Encuentra la neurona ganadora
        distances = np.zeros(num_neurons)  # Distancias de cada neurona
        for i in range(num_neurons[0]):
            for j in range(num_neurons[1]):
                distances[i, j] = euclidean_distance(weights[i, j], input_vector)

        winner_idx = np.unravel_index(np.argmin(distances), distances.shape)  # Índice de la neurona ganadora

        # Actualización de pesos de la neurona ganadora y vecinas
        for i in range(num_neurons[0]):
            for j in range(num_neurons[1]):
                if euclidean_distance(np.array(winner_idx), (i, j)) < 2:  # Vecindad
                    weights[i, j] = update_weights(weights[i, j], input_vector, learning_rate)

# Visualización del mapa
plt.figure(figsize=(10, 8))
plt.scatter(weights[:, :, 0].flatten(), weights[:, :, 1].flatten(), c='red', marker='x', label='Neuronas')
plt.scatter(data[:, 0], data[:, 1], c='blue', marker='o', alpha=0.5, label='Datos de entrada')
plt.title('Mapas Autoorganizados de Kohonen')
plt.xlabel('Dimensión 1')
plt.ylabel('Dimensión 2')
plt.legend()
plt.grid()
plt.show()

"""
Funciones Utilitarias:

euclidean_distance(a, b): Calcula la distancia euclidiana entre dos vectores.
update_weights(weights, input_vector, learning_rate): Actualiza los pesos de una neurona hacia el vector de entrada utilizando la tasa de aprendizaje.
Parámetros del Mapa:

Definimos el número de neuronas en la cuadrícula, el número de iteraciones y la tasa de aprendizaje inicial.
Inicialización de Pesos:

Los pesos de las neuronas se inicializan aleatoriamente en un rango [0, 1].
Generación de Datos de Entrada:

Creamos un conjunto de datos aleatorios de 100 puntos en 2D.
Entrenamiento del Mapa:

Para cada iteración, ajustamos la tasa de aprendizaje utilizando un decaimiento exponencial.
Para cada vector de entrada, encontramos la neurona ganadora, es decir, la neurona con el peso más cercano.
Actualizamos los pesos de la neurona ganadora y sus vecinas.
Visualización:

Se utilizan gráficos para mostrar la ubicación de las neuronas en el espacio y los datos de entrada.
"""