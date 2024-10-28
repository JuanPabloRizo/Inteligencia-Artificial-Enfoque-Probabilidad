import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Cargamos el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizamos las imágenes para que los valores de los píxeles estén entre 0 y 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Convertimos las etiquetas a una representación categórica
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definimos el modelo de red neuronal
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Aplanamos la entrada de 28x28 a un vector de 784
    Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y función de activación ReLU
    Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una para cada dígito) y activación softmax
])

# Compilamos el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamos el modelo
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Evaluamos el modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')

# Función para predecir dígitos manuscritos en una imagen
def predict_digit(image):
    image = cv2.resize(image, (28, 28))  # Redimensionamos la imagen a 28x28
    image = image.astype('float32') / 255.0  # Normalizamos la imagen
    image = np.expand_dims(image, axis=0)  # Agregamos una dimensión para el lote
    predictions = model.predict(image)  # Realizamos la predicción
    predicted_digit = np.argmax(predictions)  # Obtenemos el dígito predicho
    return predicted_digit

# Cargamos una imagen de prueba (por ejemplo, una imagen de dígito manuscrito)
test_image = cv2.imread('digit.png', cv2.IMREAD_GRAYSCALE)  # Asegúrate de que la imagen esté en escala de grises
predicted_digit = predict_digit(test_image)
print(f'Predicted digit: {predicted_digit}')
"""
Carga de Datos: Cargamos el conjunto de datos MNIST, que contiene imágenes de dígitos manuscritos, y las dividimos en conjuntos de entrenamiento y prueba.

Preprocesamiento:

Las imágenes se normalizan a un rango entre 0 y 1 para facilitar el entrenamiento del modelo.
Las etiquetas se convierten en formato categórico para la clasificación (one-hot encoding).
Modelo de Red Neuronal:

Se define un modelo secuencial que incluye una capa de entrada que aplana la imagen de 28x28 a un vector de 784 elementos, una capa oculta con 128 neuronas y una capa de salida con 10 neuronas (una para cada dígito).
Compilación y Entrenamiento: Se compila el modelo utilizando el optimizador Adam y la función de pérdida categorical crossentropy, y luego se entrena el modelo con el conjunto de datos.

Evaluación: Se evalúa el modelo en el conjunto de prueba para obtener la precisión.

Predicción: Se define una función predict_digit que toma una imagen de un dígito manuscrito, la redimensiona y normaliza, y luego utiliza el modelo para predecir el dígito.
"""