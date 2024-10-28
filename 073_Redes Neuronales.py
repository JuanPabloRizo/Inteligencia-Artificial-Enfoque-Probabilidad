import numpy as np

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide (para el cálculo del gradiente)
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada (4 ejemplos con 3 características)
X = np.array([[0, 0, 1],
              [1, 1, 1],
              [1, 0, 1],
              [0, 1, 1]])

# Salidas reales (etiquetas)
y = np.array([[0], [1], [1], [0]])

# Semilla para hacer reproducible el código
np.random.seed(1)

# Inicializar pesos aleatorios con una media de 0
# Pesos entre la capa de entrada y la capa oculta (3 entradas -> 4 neuronas en la capa oculta)
weights_0_1 = 2 * np.random.random((3, 4)) - 1

# Pesos entre la capa oculta y la capa de salida (4 neuronas en la capa oculta -> 1 neurona de salida)
weights_1_2 = 2 * np.random.random((4, 1)) - 1

# Definir la tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la red neuronal
for epoch in range(10000):
    # Paso 1: Propagación hacia adelante
    layer_0 = X  # Entrada de la red

    # Cálculo de la salida de la capa oculta
    layer_1 = sigmoid(np.dot(layer_0, weights_0_1))

    # Cálculo de la salida de la capa final
    layer_2 = sigmoid(np.dot(layer_1, weights_1_2))

    # Paso 2: Cálculo del error (diferencia entre predicción y etiqueta real)
    layer_2_error = y - layer_2

    if (epoch % 1000) == 0:
        print(f"Error en la iteración {epoch}: {np.mean(np.abs(layer_2_error))}")

    # Paso 3: Propagación hacia atrás (retropropagación del error)
    # Gradiente de la salida
    layer_2_delta = layer_2_error * sigmoid_derivative(layer_2)

    # Calcular el error de la capa oculta (basado en la salida de la capa final)
    layer_1_error = layer_2_delta.dot(weights_1_2.T)

    # Gradiente de la capa oculta
    layer_1_delta = layer_1_error * sigmoid_derivative(layer_1)

    # Paso 4: Actualización de los pesos
    weights_1_2 += layer_1.T.dot(layer_2_delta) * learning_rate
    weights_0_1 += layer_0.T.dot(layer_1_delta) * learning_rate

# Predicciones finales después del entrenamiento
print("Predicciones después del entrenamiento:")
print(layer_2)
"""
Funciones de activación y derivadas:

sigmoid(x): Es una función de activación que transforma la entrada en un valor entre 0 y 1. Se usa para modelar probabilidades.
sigmoid_derivative(x): Calcula la derivada de la función sigmoide, utilizada en la retropropagación para ajustar los pesos.
Inicialización de pesos:
Los pesos entre capas son inicializados aleatoriamente con valores entre -1 y 1. Se necesita para garantizar que los pesos empiecen de manera diferente.

Propagación hacia adelante:

layer_1 = sigmoid(np.dot(layer_0, weights_0_1)): Multiplicamos las entradas por los pesos de la capa oculta y aplicamos la función sigmoide para obtener las activaciones de la capa oculta.
layer_2 = sigmoid(np.dot(layer_1, weights_1_2)): Lo mismo se repite para la capa de salida.
Error y retropropagación:

Calculamos el error como la diferencia entre las salidas predichas y las etiquetas reales.
Luego, retropropagamos el error ajustando los pesos de las capas usando el gradiente de la función de activación.
Actualización de pesos:
Los pesos se ajustan basados en el gradiente de la función de activación, la tasa de aprendizaje, y el error calculado.

Salida esperada:
Durante el entrenamiento, se imprime el error medio en cada 1000 iteraciones, y al final se muestran las predicciones del modelo entrenado.
"""