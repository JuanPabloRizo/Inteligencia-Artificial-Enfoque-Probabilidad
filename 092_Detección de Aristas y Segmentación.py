import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas
import cv2  # Importa la biblioteca OpenCV para procesamiento de imágenes

# Función para clasificar la imagen
def Clasificador(imagenc):
    # Muestra la imagen original
    cv2.imshow('imagen Original', imagenc)
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra las ventanas de OpenCV

    # Obtiene las dimensiones de la imagen
    m, n, c = imagenc.shape
    # Crea una nueva imagen en blanco y negro (0s y 255s)
    imagenb = np.zeros((m, n))

    # Recorre cada píxel de la imagen original
    for x in range(m):
        for y in range(n):
            # Clasifica el píxel en función de sus valores RGB
            if (0 < imagenc[x, y, 0] < 200) and (0 < imagenc[x, y, 1] < 200) and (0 < imagenc[x, y, 2] < 200):
                imagenb[x, y] = 0  # Si el píxel está en el rango definido, se convierte a negro
            else:
                imagenb[x, y] = 255  # De lo contrario, se convierte a blanco

    # Muestra la imagen clasificada
    cv2.imshow('imagen clasificada', imagenb)
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra las ventanas de OpenCV

    # Guarda la imagen clasificada como 'Resultado.jpg'
    cv2.imwrite('Resultado.jpg', imagenb)

if __name__ == "__main__":
    # Carga la imagen original
    ladrillos = cv2.imread('imagen.jpg')
    
    # Llama a la función de clasificación
    Clasificador(ladrillos)

    # Carga la imagen clasificada en escala de grises
    imagen = cv2.imread("Resultado.jpg", 0)

    # Define un kernel para detectar bordes horizontales
    kernel_horizontal = np.array([[1, 1, 1],
                                  [0, 0, 0],
                                  [-1, -1, -1]])

    # Define un kernel para detectar bordes verticales
    kernel_vertical = np.array([[1, 0, -1],
                                [1, 0, -1],
                                [1, 0, -1]])

    # Obtiene las dimensiones de la imagen
    m, n = imagen.shape

    # Crea matrices vacías para almacenar los resultados de los filtros
    filtro_horizontal = np.zeros_like(imagen)  # Para bordes horizontales
    filtro_vertical = np.zeros_like(imagen)  # Para bordes verticales

    # Aplicar la convolución para bordes horizontales
    for x in range(m - 2):  # Evita el borde de la imagen
        for y in range(n - 2):
            # Aplica la convolución con el kernel horizontal
            res_hor = np.sum(imagen[x:x + 3, y:y + 3] * kernel_horizontal)
            # Umbral para determinar si es un borde horizontal
            if res_hor > 250:
                filtro_horizontal[x, y] = 255  # Se asigna el valor máximo si es un borde

    # Aplicar la convolución para bordes verticales
    for x in range(m - 2):  # Evita el borde de la imagen
        for y in range(n - 2):
            # Aplica la convolución con el kernel vertical
            res_vert = np.sum(imagen[x:x + 3, y:y + 3] * kernel_vertical)
            # Umbral para determinar si es un borde vertical
            if res_vert > 250:
                filtro_vertical[x, y] = 255  # Se asigna el valor máximo si es un borde

    # Calcular la magnitud del vector gradiente
    magnitud_gradiente = np.sqrt(filtro_horizontal ** 2 + filtro_vertical ** 2)
    # Normalizar la magnitud del gradiente para que esté entre 0 y 255
    magnitud_gradiente = np.clip(magnitud_gradiente, 0, 255)
    # Convertir a tipo de dato uint8
    magnitud_gradiente = magnitud_gradiente.astype(np.uint8)

    # Mostrar los bordes horizontales detectados
    cv2.imshow("Bordes Horizontales", filtro_horizontal)
    cv2.imwrite('Bordes Horizontales.jpg', filtro_horizontal)  # Guardar la imagen de bordes horizontales

    # Mostrar los bordes verticales detectados
    cv2.imshow("Bordes Verticales", filtro_vertical)
    cv2.imwrite('Bordes Verticales.jpg', filtro_vertical)  # Guardar la imagen de bordes verticales

    # Mostrar la combinación de ambos bordes
    filtro_combined = cv2.bitwise_or(filtro_horizontal, filtro_vertical)  # Combina los bordes
    cv2.imshow("Bordes Combinados", filtro_combined)
    cv2.imwrite('Bordes Combinados.jpg', filtro_combined)  # Guardar la imagen de bordes combinados

    # Imprimir la magnitud del gradiente y su máximo
    print(magnitud_gradiente)
    print(np.max(magnitud_gradiente))

    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV

"""
Importaciones:

Se importan las bibliotecas necesarias: numpy para operaciones numéricas y cv2 para procesamiento de imágenes.
Función Clasificador:

Esta función clasifica los píxeles de la imagen en blanco o negro basándose en sus valores RGB.
Se muestra la imagen original y se crea una imagen en blanco y negro donde los píxeles que cumplen con una condición (valores RGB menores a 200) se convierten a negro, y el resto a blanco.
Carga de la imagen:

En el bloque if __name__ == "__main__":, se carga la imagen original y se llama a la función Clasificador.
Detección de Bordes:

Se definen dos kernels (uno para bordes horizontales y otro para bordes verticales).
Se realiza la convolución de la imagen clasificada con estos kernels para detectar los bordes. La convolución se realiza en dos bucles anidados, donde se aplica el kernel a cada píxel de la imagen.
Magnitud del Gradiente:

Se calcula la magnitud del gradiente combinando los resultados de los filtros horizontal y vertical.
Visualización y Guardado:

Se muestran y guardan las imágenes resultantes: bordes horizontales, bordes verticales y bordes combinados.
Salida de la Magnitud:

Se imprimen la magnitud del gradiente y su valor máximo.
"""