import numpy as np

# Función de activación (sigmoide) y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada (4 ejemplos, 2 características)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Salidas esperadas (XOR)
y = np.array([[0], [1], [1], [0]])

# Inicialización de pesos aleatorios
np.random.seed(42)
weights_input_hidden = np.random.rand(2, 2)  # 2 neuronas en la capa oculta
weights_hidden_output = np.random.rand(2, 1)  # 1 neurona en la capa de salida

# Parámetros de entrenamiento
epochs = 10000
learning_rate = 0.1

# Entrenamiento
for epoch in range(epochs):
    # Propagación hacia adelante
    hidden_layer_input = np.dot(X, weights_input_hidden)  # Entradas a la capa oculta
    hidden_layer_output = sigmoid(hidden_layer_input)      # Salida de la capa oculta

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)  # Entradas a la capa de salida
    predicted_output = sigmoid(output_layer_input)      # Salida de la capa de salida

    # Cálculo del error
    error = y - predicted_output

    # Retropropagación
    d_predicted_output = error * sigmoid_derivative(predicted_output)  # Derivada de la salida
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)  # Error en la capa oculta
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)  # Derivada de la capa oculta

    # Actualización de pesos
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# Resultados finales
print("Salida después del entrenamiento:")
print(predicted_output)

"""
Funciones de Activación:

Definimos la función sigmoide y su derivada. La función sigmoide se utiliza como activación, y su derivada se usará durante la retropropagación.
Datos de Entrada y Salidas Esperadas:

Creamos un conjunto de datos simple para el problema XOR, donde la salida esperada es 0 o 1 según la operación lógica.
Inicialización de Pesos:

Inicializamos los pesos de manera aleatoria para las conexiones entre la capa de entrada y la capa oculta, así como entre la capa oculta y la capa de salida.
Entrenamiento:

Durante un número determinado de épocas (10,000 en este caso), realizamos la propagación hacia adelante para calcular la salida de la red.
Calculamos el error al comparar la salida predicha con la salida esperada.
Aplicamos retropropagación para calcular el gradiente del error con respecto a los pesos y actualizamos los pesos utilizando la tasa de aprendizaje.
Resultados Finales:

Al final del entrenamiento, imprimimos la salida de la red para ver cómo se ha ajustado a los datos de entrada.
"""