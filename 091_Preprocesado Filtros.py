import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas.
import cv2  # Importa OpenCV para procesamiento de imágenes.

# Función para agregar ruido gaussiano a una imagen
def gaussiano(img):
    # Extraer el canal verde de la imagen (index 1)
    img_gray = img[:, :, 1]  
    # Generar ruido gaussiano con media 0 y desviación estándar de 50
    noise = np.random.normal(0, 50, img_gray.shape)  
    # Añadir el ruido a la imagen
    img_noised = img_gray + noise  
    # Asegurarse de que los valores de píxeles estén entre 0 y 255
    img_noised = np.clip(img_noised, 0, 255).astype(np.uint8)  
    # Mostrar la imagen con ruido
    cv2.imshow('Ruido Gaussiano', img_noised)  
    # Guardar la imagen con ruido
    cv2.imwrite('ruido gaus.jpg', img_noised)  
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas

# Función para agregar ruido de sal y pimienta a una imagen
def salpim(img):
    # Extraer el canal verde de la imagen (index 1)
    img_gray = img[:, :, 1]  
    img_size = img_gray.size  # Obtener el tamaño de la imagen
    noise_percentage = 0.1  # Porcentaje de píxeles que serán ruido
    noise_size = int(noise_percentage * img_size)  # Cantidad de ruido a agregar
    random_indices = np.random.choice(img_size, noise_size)  # Índices aleatorios para el ruido
    img_noised = img_gray.copy()  # Copiar la imagen original
    # Seleccionar valores de ruido de los valores mínimo y máximo de la imagen
    noise = np.random.choice([img_gray.min(), img_gray.max()], noise_size)  
    # Reemplazar los píxeles seleccionados con ruido
    img_noised.flat[random_indices] = noise  
    # Mostrar la imagen con ruido
    cv2.imshow('Ruido Sal y Pimienta', img_noised)  
    # Guardar la imagen con ruido
    cv2.imwrite('ruido sp.jpg', img_noised)  
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas

# Filtro de media
def media(img):
    # Definir un kernel de 3x3 para el filtro de media
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])  
    m, n = img.shape  # Obtener dimensiones de la imagen
    filtro = np.zeros_like(img)  # Crear una imagen vacía del mismo tamaño
    
    # Aplicar el filtro de media
    for x in range(m - 2):  # Recorrer filas
        for y in range(n - 2):  # Recorrer columnas
            # Calcular la suma ponderada de los píxeles en la vecindad
            res = np.sum(img[x:x + 3, y:y + 3] * kernel)  
            # Guardar el resultado en la imagen filtrada
            filtro[x, y] = res * (1 / 9)  # Dividir por 9 para obtener el promedio
    return filtro  # Retornar la imagen filtrada

if __name__ == "__main__":
    img = cv2.imread('imagen.jpg')  # Leer la imagen original
    cv2.imshow('imagen Original', img)  # Mostrar la imagen original
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas

    # Agregar ruido gaussiano a la imagen
    gaussiano(img)  
    gaus = cv2.imread('ruido gaus.jpg', 0)  # Leer la imagen con ruido gaussiano

    # Agregar ruido de sal y pimienta a la imagen
    salpim(img)  
    sp = cv2.imread('ruido sp.jpg', 0)  # Leer la imagen con ruido sal y pimienta

    # Aplicar filtro de media a la imagen con ruido gaussiano
    media_gaus = media(gaus)  
    cv2.imwrite('Filtro media con ruido gaus.jpg', media_gaus)  # Guardar imagen filtrada
    cv2.imshow("Filtro media con gaus", media_gaus)  # Mostrar imagen filtrada
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()  # Cierra todas las ventanas
    
    # Aplicar filtro de media a la imagen con ruido sal y pimienta
    media_sp = media(sp)  
    cv2.imwrite('Filtro media con sp.jpg', media_sp)  # Guardar imagen filtrada
    cv2.imshow("Filtro media con sp", media_sp)  # Mostrar imagen filtrada
    cv2.waitKey(0)  # Espera a que se presione una tecla
    cv2.destroyAllWindows()

    # Aplicar filtro gaussiano a las imágenes con ruido
    img_filtrada_gaussiano_salpimienta = cv2.GaussianBlur(sp, (5, 5), 0)  
    img_filtrada_gaussiano_gaussiano = cv2.GaussianBlur(gaus, (5, 5), 0)  
    
    kernel = np.array([[1, 1, 1],  # Definir un kernel para filtros mínimos y máximos
                       [1, 1, 1],
                       [1, 1, 1]])
    
    # Filtro mínimo (usando erosión)
    img_filtrada_minimo_salpimienta = cv2.erode(sp, kernel)  
    img_filtrada_minimo_gaussiano = cv2.erode(gaus, kernel)  

    # Filtro máximo (usando dilatación)
    img_filtrada_maximo_salpimienta = cv2.dilate(sp, kernel)  
    img_filtrada_maximo_gaussiano = cv2.dilate(gaus, kernel)  

    # Filtro de mediana
    img_filtrada_mediana_salpimienta = cv2.medianBlur(sp, 5)  
    img_filtrada_mediana_gaussiano = cv2.medianBlur(gaus, 5)  

    # Mostrar resultados de los filtros
    cv2.imshow("Filtro gaussiano (Ruido sal-pimienta)", img_filtrada_gaussiano_salpimienta)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
    cv2.imshow("Filtro gaussiano (Ruido Gaussiano)", img_filtrada_gaussiano_gaussiano)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

    cv2.imshow("Filtro minimo (Ruido sal-pimienta)", img_filtrada_minimo_salpimienta)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
    cv2.imshow("Filtro minimo (Ruido Gaussiano)", img_filtrada_minimo_gaussiano)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

    cv2.imshow("Filtro maximo (Ruido sal-pimienta)", img_filtrada_maximo_salpimienta)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()    
    cv2.imshow("Filtro maximo (Ruido Gaussiano)", img_filtrada_maximo_gaussiano)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

    cv2.imshow("Filtro mediana (Ruido sal-pimienta)", img_filtrada_mediana_salpimienta)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()   
    cv2.imshow("Filtro mediana (Ruido Gaussiano)", img_filtrada_mediana_gaussiano)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  

    # Guardar las imágenes filtradas
    cv2.imwrite("filtro_gaussiano_salpimienta.jpg", img_filtrada_gaussiano_salpimienta)  
    cv2.imwrite("filtro_gaussiano_gaussiano.jpg", img_filtrada_gaussiano_gaussiano)  

    cv2.imwrite("filtro_minimo_salpimienta.jpg", img_filtrada_minimo_salpimienta)  
    cv2.imwrite("filtro_minimo_gaussiano.jpg", img_filtrada_minimo_gaussiano)  

    cv2.imwrite("filtro_maximo_salpimienta.jpg", img_filtrada_maximo_salpimienta)  
    cv2.imwrite("filtro_maximo_gaussiano.jpg", img_filtrada_maximo_gaussiano)  

    cv2.imwrite("filtro_mediana_salpimienta.jpg", img_filtrada_mediana_salpimienta)  
    cv2.imwrite("filtro_mediana_gaussiano.jpg", img_filtrada_mediana_gaussiano)  
