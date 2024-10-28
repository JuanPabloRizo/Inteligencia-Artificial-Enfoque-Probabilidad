import numpy as np

# Función de activación Sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Función de activación Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, x * alpha)

# Función de activación Tangente Hiperbólica (tanh)
def tanh(x):
    return np.tanh(x)

# Función de activación Softmax
def softmax(x):
    exps = np.exp(x - np.max(x))  # Para estabilidad numérica
    return exps / np.sum(exps)

# Datos de entrada
x = np.array([-1.0, 0.0, 1.0, 2.0])

# Aplicar cada función de activación
print("Sigmoide:", sigmoid(x))
print("ReLU:", relu(x))
print("Leaky ReLU:", leaky_relu(x))
print("Tangente Hiperbólica:", tanh(x))
print("Softmax:", softmax(x))  # Usualmente se aplica a un vector de clase
"""
Sigmoide: Convierte las entradas en valores entre 0 y 1. Ideal para tareas de clasificación binaria o como función de activación en capas ocultas.

ReLU: Deja pasar los valores positivos tal cual y convierte los negativos a 0. Es rápida de computar y es la elección predeterminada para redes neuronales profundas.

Leaky ReLU: Introduce una pequeña pendiente en los valores negativos, evitando el problema de que algunas neuronas se queden "muertas" con una salida constante de 0.

Tangente Hiperbólica (tanh): Similar a la sigmoide, pero con un rango de salida entre -1 y 1, lo cual puede ser beneficioso para centrar los datos.

Softmax: Convierte una lista de valores en un vector de probabilidades que suman 1. Se utiliza generalmente en la capa de salida de una red neuronal para problemas de clasificación multiclase.
"""