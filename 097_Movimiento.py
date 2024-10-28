import cv2
import numpy as np

# Cargar el video
video = cv2.VideoCapture('video_original.mp4')

# Inicializar el primer frame para el fondo como None
bgGray = None

# Definir parámetros ajustables
UMBRAL_DIFF = 15 # Umbral para la diferencia entre el fondo y el frame actual
MIN_AREA = 9000   # Área mínima de los contornos a detectar
SUAVIZADO_KERNEL = (5, 5)  # Tamaño del kernel para el suavizado gaussiano
FPS = 30  # Velocidad de cuadros por segundo (puedes ajustarlo según tu video)
ACTUALIZACION_FONDO = True  # Controlar si el fondo se actualiza con cada frame

while True:
    ret, frame = video.read()
    if not ret:
        break  # Salir si no hay más frames

    # Convertir el frame actual a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicar suavizado gaussiano para reducir el ruido
    gray_suavizado = cv2.GaussianBlur(gray, SUAVIZADO_KERNEL, 0)

    # Inicializar el fondo con el primer frame si es None
    if bgGray is None:
        bgGray = gray_suavizado
        continue  # Saltar al siguiente frame si el fondo aún no está definido

    # Calcular la diferencia absoluta entre el frame actual suavizado y el fondo
    dif = cv2.absdiff(gray_suavizado, bgGray)

    # Aplicar un umbral a la diferencia
    _, th = cv2.threshold(dif, UMBRAL_DIFF, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen umbralizada
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar rectángulos alrededor de los objetos detectados si el área es mayor que el valor mínimo
    for c in cnts:
        area = cv2.contourArea(c)
        if area > MIN_AREA:  # Ajusta el área mínima según tus necesidades
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el frame con detección
    cv2.imshow('Frame', frame)

    # Actualizar el fondo con un promedio ponderado (opcional)
    if ACTUALIZACION_FONDO:
        # El fondo se actualiza gradualmente con el frame actual
        bgGray = cv2.addWeighted(bgGray, 0.9, gray_suavizado, 0.1, 0)

    # Esperar hasta que se presione 'q' para salir
    if cv2.waitKey(1000 // FPS) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
cv2.destroyAllWindows()
