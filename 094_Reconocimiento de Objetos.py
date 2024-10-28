import cv2 as cv  # Importamos la biblioteca OpenCV para procesamiento de imágenes
import numpy as np  # Importamos NumPy para operaciones numéricas
from matplotlib import pyplot as plt  # Importamos pyplot para visualizar las imágenes

# Cargamos la imagen en escala de grises
img = cv.imread('imagen.jpg', cv.IMREAD_GRAYSCALE)
# Verificamos que la imagen se haya cargado correctamente
assert img is not None, "file could not be read, check with os.path.exists()"

# Hacemos una copia de la imagen original para no modificarla
img2 = img.copy()

# Cargamos la imagen de plantilla también en escala de grises
template = cv.imread('imagen2.jpg', cv.IMREAD_GRAYSCALE)
# Verificamos que la plantilla se haya cargado correctamente
assert template is not None, "file could not be read, check with os.path.exists()"

# Obtenemos el ancho (w) y la altura (h) de la plantilla
w, h = template.shape[::-1]

# Definimos una lista de métodos para comparación de plantillas
methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
            'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']

# Iteramos sobre cada método de comparación
for meth in methods:
    img = img2.copy()  # Reiniciamos img a la copia original

    # Obtenemos el método de comparación usando getattr para acceder dinámicamente
    method = getattr(cv, meth)

    # Aplicamos el método de coincidencia de plantillas
    res = cv.matchTemplate(img, template, method)
    
    # Obtenemos los valores mínimo y máximo y sus ubicaciones en la imagen resultante
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # Si el método es TM_SQDIFF o TM_SQDIFF_NORMED, tomamos el mínimo
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc  # La esquina superior izquierda de la coincidencia
    else:
        top_left = max_loc  # La esquina superior izquierda de la coincidencia

    # Calculamos la esquina inferior derecha del rectángulo delimitador
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Dibujamos un rectángulo alrededor de la coincidencia encontrada en la imagen
    cv.rectangle(img, top_left, bottom_right, 255, 2)

    # Visualizamos el resultado de la coincidencia
    plt.subplot(121), plt.imshow(res, cmap='gray')  # Muestra el resultado de la coincidencia en gris
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])  # Título y ocultar ticks
    plt.subplot(122), plt.imshow(img, cmap='gray')  # Muestra la imagen original con el rectángulo
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])  # Título y ocultar ticks
    plt.suptitle(meth)  # Título general con el método utilizado

    plt.show()  # Muestra las imágenes

"""
Importación de Bibliotecas:

Se importan las bibliotecas necesarias para el procesamiento de imágenes y la visualización.
Carga de Imágenes:

Las imágenes se cargan en escala de grises, lo que es común en técnicas de procesamiento de imágenes donde los colores no son relevantes.
Verificación de Carga:

Se utiliza assert para asegurarse de que las imágenes se han cargado correctamente. Si no es así, se lanza un mensaje de error.
Definición de Métodos de Coincidencia:

Se crea una lista con diferentes métodos de coincidencia de plantillas que OpenCV proporciona.
Iteración sobre Métodos:

Para cada método en la lista, se realiza el siguiente proceso:
Se copia la imagen original para no modificarla.
Se obtiene el método correspondiente usando getattr.
Se aplica el método de coincidencia de plantillas a la imagen.
Se determinan los valores mínimo y máximo del resultado, así como sus ubicaciones.
Dependiendo del método utilizado, se elige la ubicación de coincidencia adecuada (mínima o máxima).
Se dibuja un rectángulo alrededor de la coincidencia encontrada.
Visualización:

Se utilizan subgráficas de matplotlib para mostrar tanto el resultado de la coincidencia como la imagen 
original con el rectángulo dibujado, permitiendo comparar visualmente los resultados de los diferentes métodos.
"""