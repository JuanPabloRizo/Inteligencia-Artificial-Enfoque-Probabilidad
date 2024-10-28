import numpy as np
import random

# Generar datos de ejemplo: combinamos dos grupos de datos en dos dimensiones.
# Un grupo centrado en (2,2) y otro grupo centrado en (7,7).
# Cada grupo tiene 50 puntos generados aleatoriamente con una desviación estándar de 0.5.
np.random.seed(42)  # Fijamos la semilla para que los resultados sean reproducibles
datos = np.vstack((np.random.normal([2, 2], 0.5, size=(50, 2)),
                   np.random.normal([7, 7], 0.5, size=(50, 2))))

# Función para calcular la distancia euclidiana entre dos puntos a y b.
# La distancia euclidiana es la raíz cuadrada de la suma de los cuadrados de las diferencias.
def calcular_distancia(a, b):
    return np.sqrt(np.sum((a - b)**2))  # Distancia entre dos puntos en el espacio 2D

# Inicializar los centroides aleatoriamente eligiendo k puntos del conjunto de datos.
def inicializar_centroides(datos, k):
    # Seleccionamos k índices aleatorios del conjunto de datos.
    indices = random.sample(range(datos.shape[0]), k)
    # Los centroides iniciales son los puntos correspondientes a esos índices.
    return datos[indices, :]

# Asignar cada punto de datos al clúster cuyo centroide está más cerca.
def asignar_clustres(datos, centroides):
    asignaciones = []  # Aquí almacenamos a qué clúster pertenece cada punto
    for punto in datos:
        # Calculamos la distancia del punto actual a cada uno de los centroides.
        distancias = [calcular_distancia(punto, centroide) for centroide in centroides]
        # Asignamos el punto al clúster cuyo centroide esté más cerca (mínima distancia).
        asignaciones.append(np.argmin(distancias))  # np.argmin devuelve el índice del centroide más cercano
    return asignaciones

# Recalcular los centroides como la media de los puntos asignados a cada clúster.
def recalcular_centroides(datos, asignaciones, k):
    nuevos_centroides = []  # Almacenamos los nuevos centroides
    for i in range(k):
        # Filtramos los puntos que pertenecen al clúster i
        puntos_clust = datos[np.array(asignaciones) == i]
        # Calculamos el nuevo centroide como la media de esos puntos.
        nuevos_centroides.append(np.mean(puntos_clust, axis=0))  # Media por columnas (x, y)
    return np.array(nuevos_centroides)  # Devolvemos los nuevos centroides como un array

# Algoritmo K-Means principal
def kmeans(datos, k, max_iter=100):
    # Inicializamos los centroides aleatoriamente
    centroides = inicializar_centroides(datos, k)
    
    # Repetimos el proceso hasta un máximo de 'max_iter' iteraciones
    for _ in range(max_iter):
        # Asignar cada punto al clúster más cercano (basado en los centroides actuales)
        asignaciones = asignar_clustres(datos, centroides)
        
        # Recalcular los centroides basados en las nuevas asignaciones
        nuevos_centroides = recalcular_centroides(datos, asignaciones, k)
        
        # Si los centroides no cambian, hemos convergido y podemos detenernos
        if np.all(centroides == nuevos_centroides):  # np.all verifica si todos los valores son iguales
            break  # Terminamos el bucle si los centroides no cambian
        
        # Actualizamos los centroides para la siguiente iteración
        centroides = nuevos_centroides
    
    return centroides, asignaciones  # Devolvemos los centroides finales y las asignaciones de clúster

# Ejecución del algoritmo K-Means con k=2 (queremos agrupar los datos en 2 clústeres)
k = 2
centroides_finales, asignaciones_finales = kmeans(datos, k)

# Mostrar los resultados
print("Centroides finales:")
print(centroides_finales)  # Muestra las coordenadas de los centroides finales
# Convertir las asignaciones a una lista regular de enteros y luego imprimirlas
print("\nAsignaciones de clúster para cada punto de datos:")
print(list(map(int, asignaciones_finales)))  # Convertimos cada valor a un entero y luego 
"""
Generación de datos:

Se generan dos grupos de datos usando una distribución normal centrada en dos puntos diferentes. Estos son nuestros datos de ejemplo para el agrupamiento.
Función de distancia:
calcular_distancia(a, b) calcula la distancia euclidiana entre dos puntos 
a y b.
Inicialización de centroides:
inicializar_centroides(datos, k) selecciona aleatoriamente k puntos de los 
datos como los centroides iniciales.
Asignación de clúster:
asignar_clustres(datos, centroides) asigna cada punto al clúster cuyo centroide está más cercano.
Recalcular centroides:
recalcular_centroides(datos, asignaciones, k) actualiza la posición de cada centroide tomando la media de todos los puntos asignados a ese clúster.
Algoritmo K-Means:
kmeans(datos, k, max_iter) es el algoritmo principal que repite la asignación de puntos a clústeres y la recalculación de centroides hasta que los centroides ya no cambian.
Resultado esperado:
Este código imprimirá los centroides finales (las posiciones calculadas para los dos clústeres) y las asignaciones de clústeres para cada punto de datos.
"""