import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = cv2.imread('imagen.jpg')
# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de Canny para detectar bordes
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Aplicar la Transformada de Hough para detectar líneas
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=10)

# Dibujar las líneas detectadas en la imagen original
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # Dibujar la línea en la imagen
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Calcular la pendiente y la intersección para etiquetar la línea
        if x2 - x1 != 0:  # Evitar división por cero
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            # Etiquetar la línea con su ecuación
            equation = f'y = {slope:.2f}x + {intercept:.2f}'
            cv2.putText(img, equation, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Mostrar la imagen original con las líneas detectadas y etiquetadas
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Líneas Detectadas y Etiquetadas')
plt.axis('off')  # No mostrar los ejes
plt.show()

# Guardar la imagen resultante
cv2.imwrite('imagen_lineas_etiquetadas.jpg', img)
"""
Carga de la Imagen: Se carga la imagen utilizando cv2.imread.

Conversión a Escala de Grises: La imagen se convierte a escala de grises con cv2.cvtColor para facilitar la detección de bordes.

Detección de Bordes: Se aplica el filtro de Canny (cv2.Canny) para detectar bordes en la imagen. Los parámetros de umbral pueden ajustarse según la imagen.

Detección de Líneas:

Se utiliza la función cv2.HoughLinesP para detectar líneas en la imagen. Esta función devuelve las líneas en formato de coordenadas.
Los parámetros como el umbral, la longitud mínima de la línea y la distancia máxima entre segmentos de línea pueden ajustarse para mejorar la detección.
Dibujo de Líneas: Para cada línea detectada, se dibuja sobre la imagen original usando cv2.line.

Cálculo y Etiquetado de Líneas:

Se calcula la pendiente y la intersección de cada línea.
Se usa cv2.putText para etiquetar la línea con su ecuación.
Visualización: Se muestra la imagen resultante con matplotlib y se guarda en el disco con cv2.imwrite.
"""