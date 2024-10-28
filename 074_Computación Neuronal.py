import numpy as np

# Definir la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada: 4 ejemplos con 2 características cada uno
X = np.array([[0, 0], 
              [0, 1], 
              [1, 0], 
              [1, 1]])

# Salida esperada (OR lógico)
y = np.array([[0], [1], [1], [1]])

# Inicializar pesos aleatorios (2 entradas -> 1 salida)
np.random.seed(1)
weights = 2 * np.random.random((2, 1)) - 1

# Tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la neurona
for epoch in range(10000):
    # Paso 1: Propagación hacia adelante
    inputs = X
    # Producto punto entre las entradas y los pesos
    output = sigmoid(np.dot(inputs, weights))

    # Paso 2: Cálculo del error
    error = y - output
    
    # Paso 3: Retropropagación del error
    adjustments = error * sigmoid_derivative(output)
    
    # Paso 4: Ajuste de los pesos
    weights += np.dot(inputs.T, adjustments) * learning_rate

# Mostrar los resultados
print("Pesos entrenados:")
print(weights)

# Predicciones finales
print("Predicciones:")
print(sigmoid(np.dot(X, weights)))
"""
Función de activación (sigmoide):
La función sigmoide transforma la entrada de la neurona en un valor entre 0 y 1, lo cual es útil para modelar probabilidades.

Entradas y salidas:
Los datos de entrada son un conjunto de 4 ejemplos binarios, 
que representan las combinaciones posibles de dos variables. La salida esperada es el resultado de la operación OR lógico entre las dos entradas.

Inicialización de pesos:
Los pesos son inicializados con valores aleatorios entre -1 y 1. Al inicio del entrenamiento, los pesos son incorrectos y se ajustan a lo largo de varias iteraciones.

Propagación hacia adelante:
Para cada entrada, se calcula la salida de la neurona multiplicando las entradas por los pesos y aplicando la función de activación sigmoide.

Cálculo del error y retropropagación:
El error se calcula como la diferencia entre la salida esperada y la predicha. Luego, el error se retropropaga ajustando los pesos 
de acuerdo con el gradiente de la función sigmoide.

Ajuste de pesos:
Los pesos se actualizan después de cada iteración para minimizar el error y mejorar la precisión de las predicciones.

Salida esperada:
Después del entrenamiento, el modelo debería ajustar los pesos de tal manera que las predicciones finales sean muy cercanas 
a la salida esperada para la operación OR. Las predicciones serán valores entre 0 y 1, que se pueden redondear a 0 o 1 para interpretar los resultados.
"""