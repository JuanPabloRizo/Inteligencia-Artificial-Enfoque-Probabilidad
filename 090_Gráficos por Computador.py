import matplotlib.pyplot as plt
import numpy as np

# Crear una nueva figura
plt.figure(figsize=(8, 6))

# Dibujar un círculo
circle = plt.Circle((0.5, 0.5), 0.2, color='blue', alpha=0.5, label='Círculo')
plt.gca().add_artist(circle)

# Dibujar un rectángulo
rectangle = plt.Rectangle((0.1, 0.1), 0.3, 0.2, color='green', alpha=0.5, label='Rectángulo')
plt.gca().add_artist(rectangle)

# Dibujar una línea
x = np.linspace(0, 1, 100)
y = 0.5 * x + 0.2  # Ecuación de la línea: y = 0.5x + 0.2
plt.plot(x, y, color='red', label='Línea')

# Configuración de los ejes
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Títulos y etiquetas
plt.title('Ejemplo de Gráficos 2D')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
"""
Importaciones:

matplotlib.pyplot: Biblioteca para crear gráficos.
numpy: Biblioteca para trabajar con arreglos y realizar cálculos numéricos.
Crear una Nueva Figura:

plt.figure(figsize=(8, 6)): Inicializa una nueva figura con un tamaño específico.
Dibujar Formas:

plt.Circle(): Crea un círculo con un centro y un radio específicos.
plt.Rectangle(): Crea un rectángulo especificando la esquina inferior izquierda, el ancho y la altura.
plt.plot(): Traza una línea utilizando datos de puntos en los ejes x e y.
Configuración de los Ejes:

plt.xlim(0, 1) y plt.ylim(0, 1): Establecen los límites de los ejes x e y.
Se añaden líneas de referencia (horizontales y verticales) y una cuadrícula.
Títulos y Etiquetas:

plt.title(), plt.xlabel(), plt.ylabel(): Añaden títulos y etiquetas a los ejes.
plt.legend(): Muestra una leyenda para identificar las formas dibujadas.
Mostrar el Gráfico:

plt.show(): Muestra el gráfico en una ventana.
"""