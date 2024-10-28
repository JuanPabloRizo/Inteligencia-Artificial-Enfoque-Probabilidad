import numpy as np
from collections import Counter

# Datos de entrenamiento (X) y sus etiquetas (y)
X_train = np.array([[1, 1], [2, 2], [3, 3], [6, 6], [7, 7], [8, 8]])
y_train = np.array([0, 0, 0, 1, 1, 1])  # 0 es clase A, 1 es clase B

# Nuevo punto de datos que queremos clasificar
new_point = np.array([5, 5])

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# k-NN: Clasifica el nuevo punto basado en k vecinos más cercanos
def k_nearest_neighbors(X_train, y_train, new_point, k=3):
    # Calcular las distancias entre el nuevo punto y todos los puntos de entrenamiento
    distances = [euclidean_distance(x, new_point) for x in X_train]
    
    # Ordenar por distancia y seleccionar los k vecinos más cercanos
    k_indices = np.argsort(distances)[:k]
    
    # Obtener las etiquetas de los vecinos más cercanos
    k_nearest_labels = [y_train[i] for i in k_indices]
    
    # Retornar la clase más común entre los k vecinos
    most_common = Counter(k_nearest_labels).most_common(1)
    
    return most_common[0][0]

# Usar k-NN para clasificar el nuevo punto
result = k_nearest_neighbors(X_train, y_train, new_point, k=3)
print(f'El nuevo punto {new_point} ha sido clasificado como clase {result}.')
"""
Se calculan las distancias entre el nuevo punto y todos los puntos en los datos de entrenamiento.
Se seleccionan los "k" vecinos más cercanos, y luego se asigna la clase que es más común entre esos vecinos.
"""