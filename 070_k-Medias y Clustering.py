import numpy as np
import matplotlib.pyplot as plt
# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Clase que implementa el algoritmo k-medias
class KMeans:
    def __init__(self, k=2, max_iters=100):
        self.k = k  # Número de clústeres
        self.max_iters = max_iters  # Número máximo de iteraciones
        self.centroids = None  # Para almacenar los centroides
        self.clusters = None  # Para almacenar los clústeres

    def fit(self, X):
        # Inicializar aleatoriamente los centroides seleccionando k puntos de los datos
        np.random.seed(42)  # Para reproducibilidad
        initial_centroids_idx = np.random.choice(len(X), self.k, replace=False)
        self.centroids = X[initial_centroids_idx]
        
        # Iterar hasta que se cumpla el criterio de parada o se alcance el máximo de iteraciones
        for _ in range(self.max_iters):
            # Asignar cada punto al clúster más cercano
            self.clusters = self.create_clusters(X)

            # Guardar los centroides actuales para compararlos después
            previous_centroids = self.centroids.copy()

            # Recalcular los centroides (la media de todos los puntos en cada clúster)
            self.centroids = self.calculate_new_centroids(X)

            # Verificar si los centroides no han cambiado (criterio de parada)
            if self.is_converged(previous_centroids, self.centroids):
                break

    def create_clusters(self, X):
        clusters = [[] for _ in range(self.k)]
        for idx, point in enumerate(X):
            # Encontrar el centroide más cercano al punto
            closest_centroid = np.argmin([euclidean_distance(point, centroid) for centroid in self.centroids])
            # Asignar el punto al clúster correspondiente
            clusters[closest_centroid].append(idx)
        return clusters

    def calculate_new_centroids(self, X):
        # Calcular los nuevos centroides como la media de los puntos en cada clúster
        return np.array([X[cluster].mean(axis=0) if len(cluster) > 0 else np.zeros(X.shape[1]) for cluster in self.clusters])

    def is_converged(self, previous_centroids, new_centroids):
        # Verificar si los centroides han dejado de moverse (se han estabilizado)
        return np.all(previous_centroids == new_centroids)

    def predict(self, X):
        # Asignar a cada punto nuevo su clúster más cercano
        predictions = [np.argmin([euclidean_distance(point, centroid) for centroid in self.centroids]) for point in X]
        return np.array(predictions)

# Ejemplo de uso:

# Datos de ejemplo (10 puntos en un espacio bidimensional)
X = np.array([[1, 2], [2, 3], [3, 1], [8, 9], [9, 8], [10, 10], 
              [1, 0], [0, 1], [9, 9], [8, 8]])

# Crear el modelo k-medias con k=2 (buscamos 2 clústeres)
kmeans = KMeans(k=2)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Mostrar los centroides finales
print("Centroides finales:\n", kmeans.centroids)

# Predecir los clústeres para los mismos datos (X)
predicciones = kmeans.predict(X)

# Mostrar a qué clúster pertenece cada punto de los datos
print("Asignaciones de clúster para cada punto de datos:\n", predicciones)

# Visualizar los datos y los centroides
plt.scatter(X[:, 0], X[:, 1], c=predicciones, cmap='viridis', marker='o', label='Puntos de datos')
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c='red', marker='X', s=200, label='Centroides')
plt.title('k-Medias Clustering')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()
"""
Clase KMeans:

El constructor __init__ inicializa el número de clústeres k y el número máximo de iteraciones max_iters. Los centroides iniciales y los clústeres se inicializan como None.
Función fit:

Esta función ajusta el modelo a los datos. Comienza eligiendo aleatoriamente los centroides iniciales de entre los puntos de datos.
En cada iteración:
Asigna cada punto de datos al clúster cuyo centroide esté más cerca.
Recalcula los centroides como la media de los puntos dentro de cada clúster.
Verifica si los centroides han convergido (es decir, si no cambian de posición).
Si los centroides se estabilizan antes de alcanzar el máximo de iteraciones, el algoritmo termina.
Función create_clusters:

Asigna cada punto de datos al clúster correspondiente, encontrando el centroide más cercano.
Función calculate_new_centroids:

Calcula nuevos centroides como la media de los puntos dentro de cada clúster.
Función is_converged:

Compara los nuevos centroides con los anteriores. Si no se han movido, el algoritmo ha convergido.
Función predict:

Dado un conjunto de nuevos puntos de datos, esta función asigna a cada punto el clúster cuyo centroide esté más cerca.
Ejemplo con los datos proporcionados:
Centroides finales: Muestra los puntos que representan los centros de los dos clústeres encontrados.
Asignaciones de clúster: Indica a qué clúster pertenece cada punto de los datos.
"""