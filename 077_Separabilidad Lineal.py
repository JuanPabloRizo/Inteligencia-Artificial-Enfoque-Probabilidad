import numpy as np
import matplotlib.pyplot as plt

# Generar datos linealmente separables
np.random.seed(0)  # Para reproducibilidad
X1 = np.random.rand(50, 2) + np.array([0, 0])  # Clase 1
X2 = np.random.rand(50, 2) + np.array([1, 1])  # Clase 2

# Crear etiquetas
y1 = np.zeros(50)  # Etiquetas para la clase 1
y2 = np.ones(50)   # Etiquetas para la clase 2

# Combinar los datos y etiquetas
X = np.vstack((X1, X2))  # Apilar las clases verticalmente
y = np.concatenate((y1, y2))  # Concatenar las etiquetas

# Visualizar los datos
plt.scatter(X1[:, 0], X1[:, 1], color='red', label='Clase 1 (0)')
plt.scatter(X2[:, 0], X2[:, 1], color='blue', label='Clase 2 (1)')
plt.title('Datos Linealmente Separables')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()

# Generar datos no linealmente separables
X3 = np.random.rand(50, 2)  # Clase 3
X4 = np.random.rand(50, 2) + np.array([0.5, 0.5])  # Clase 4

# Crear etiquetas
y3 = np.zeros(50)  # Etiquetas para la clase 3
y4 = np.ones(50)   # Etiquetas para la clase 4

# Combinar los datos y etiquetas
X_nl = np.vstack((X3, X4))
y_nl = np.concatenate((y3, y4))

# Visualizar los datos no linealmente separables
plt.scatter(X3[:, 0], X3[:, 1], color='red', label='Clase 3 (0)')
plt.scatter(X4[:, 0], X4[:, 1], color='blue', label='Clase 4 (1)')
plt.title('Datos No Linealmente Separables')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()
"""
Importación de Bibliotecas:

Importamos numpy para generar datos y matplotlib.pyplot para la visualización.
Generación de Datos Linealmente Separables:

Utilizamos np.random.rand para crear dos grupos de datos (X1 y X2) que serán las clases. Los desplazamos para que estén separadas en el gráfico.
Creamos etiquetas para cada clase, donde la clase 1 tiene etiquetas de 0 y la clase 2 tiene etiquetas de 1.
Visualización:

Utilizamos plt.scatter para trazar los puntos en un gráfico. Los puntos de la clase 1 son rojos y los de la clase 2 son azules.
Se muestra un gráfico con un título, etiquetas en los ejes y una leyenda.
Generación de Datos No Linealmente Separables:

Creamos un nuevo conjunto de datos (X3 y X4) que no se puede separar linealmente. Esto se hace ajustando la posición de los puntos.
Visualización de Datos No Linealmente Separables:

Se repite el proceso de visualización para el segundo conjunto de datos, mostrando que no se puede trazar una línea que separe claramente las dos clases.
"""