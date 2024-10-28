import cv2
import numpy as np

# Función para aplicar una textura a una imagen
def aplicar_textura(imagen_base, textura, pos=(0, 0)):
    # Obtener las dimensiones de la textura
    h_textura, w_textura = textura.shape[:2]
    
    # Asegurarse de que la textura sea del mismo tamaño que la imagen base
    textura_resize = cv2.resize(textura, (imagen_base.shape[1], imagen_base.shape[0]))

    # Aplicar la textura a la imagen base
    imagen_con_textura = cv2.addWeighted(imagen_base, 0.7, textura_resize, 0.3, 0)
    
    return imagen_con_textura

# Función para simular sombras
def agregar_sombra(imagen, sombra_intensidad=100):
    # Crear una imagen de sombras
    sombra = np.zeros_like(imagen)
    
    # Crear una sombra en la parte inferior derecha de la imagen
    sombra[-100:, -100:] = sombra_intensidad
    
    # Sumar la sombra a la imagen original
    imagen_con_sombra = cv2.add(imagen, sombra)
    
    return imagen_con_sombra

# Cargar la imagen base
imagen_base = cv2.imread('imagen.jpg')

# Cargar la textura (debe ser una imagen en escala de grises)
textura = cv2.imread('textura.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar textura
imagen_con_textura = aplicar_textura(imagen_base, textura)

# Agregar sombra
imagen_final = agregar_sombra(imagen_con_textura, sombra_intensidad=100)

# Mostrar resultados
cv2.imshow('Imagen Base', imagen_base)
cv2.imshow('Imagen con Textura', imagen_con_textura)
cv2.imshow('Imagen Final con Sombra', imagen_final)

# Guardar la imagen final
cv2.imwrite('imagen_final_con_sombra.jpg', imagen_final)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Cargar la Imagen Base:

Utilizamos cv2.imread para cargar una imagen base sobre la cual aplicaremos la textura.
Aplicar Textura:

La función aplicar_textura toma la imagen base y la textura, redimensiona la textura para que coincida con el tamaño de la imagen base, y luego combina ambas usando cv2.addWeighted, donde se establece un peso de 0.7 para la imagen base y 0.3 para la textura.
Agregar Sombra:

La función agregar_sombra crea una imagen de sombra negra (con el mismo tamaño que la imagen base) y coloca una sección gris en la esquina inferior derecha. Luego, se suman los píxeles de la sombra a la imagen original con cv2.add.
Mostrar Resultados:

Usamos cv2.imshow para mostrar la imagen original, la imagen con textura y la imagen final con sombra.
Guardar la Imagen Final:

La imagen final se guarda en un archivo con cv2.imwrite.
"""