# Importar las librerías necesarias de TensorFlow y Keras
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
# Este dataset contiene imágenes de dígitos escritos a mano (0-9).
# Se divide en dos partes: 60,000 imágenes para entrenamiento y 10,000 para pruebas.
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesamiento de los datos
# Las imágenes se cargan con forma (60000, 28, 28), pero las redes convolucionales
# esperan una forma 4D (cantidad, ancho, alto, canales). Así que añadimos una dimensión extra para los canales (1 en este caso porque las imágenes son en blanco y negro).
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255
# Normalizamos los valores de los píxeles para que estén en el rango [0, 1] dividiendo entre 255.

# Construcción del modelo secuencial
# Vamos a crear un modelo de red neuronal convolucional utilizando la API `Sequential` de Keras.
model = models.Sequential()

# En lugar de input_shape en la primera capa, usamos el objeto Input
# La primera capa define la forma de entrada: imágenes de 28x28 píxeles con 1 canal (en escala de grises).
model.add(tf.keras.Input(shape=(28, 28, 1)))  # Capa de entrada

# Capa de convolución
# Se agregan 32 filtros (o kernels) de tamaño 3x3 que se aplican a la imagen de entrada. La activación 'relu' ayuda a agregar no linealidades.
model.add(layers.Conv2D(32, (3, 3), activation='relu'))

# Capa de pooling
# Pooling reduce la dimensionalidad de la imagen (en este caso, MaxPooling toma el valor máximo en una ventana 2x2).
model.add(layers.MaxPooling2D((2, 2)))

# Capa de convolución adicional
# Después de reducir el tamaño de la imagen, agregamos otra capa de convolución con 64 filtros.
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Otra capa de pooling
# Nuevamente, reducimos el tamaño de la imagen con MaxPooling.
model.add(layers.MaxPooling2D((2, 2)))

# Capa de flattening para transformar los datos en un vector 1D
# Las salidas de las capas anteriores son 2D (alto, ancho), pero las capas densas (fully connected) esperan vectores. Flatten convierte todo en un solo vector.
model.add(layers.Flatten())

# Capa completamente conectada (densa)
# Agregamos una capa densa con 64 neuronas y activación 'relu'.
model.add(layers.Dense(64, activation='relu'))

# Capa de salida
# La capa final tiene 10 neuronas (porque tenemos 10 clases: los dígitos 0-9). La activación 'softmax' se usa para convertir las salidas en probabilidades.
model.add(layers.Dense(10, activation='softmax'))

# Compilar el modelo
# Se usa el optimizador 'adam', que es un algoritmo eficiente de optimización.
# La pérdida que se minimiza es 'sparse_categorical_crossentropy', que es adecuada para clasificación multiclase cuando las etiquetas están en forma de enteros.
# 'accuracy' se utiliza como métrica para monitorear el rendimiento.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
# Entrenamos el modelo usando las imágenes y etiquetas del conjunto de entrenamiento.
# epochs=5 significa que el modelo verá todas las imágenes 5 veces.
# batch_size=64 significa que el modelo ajustará los pesos después de ver 64 imágenes a la vez.
model.fit(train_images, train_labels, epochs=5, batch_size=64)

# Evaluar el modelo en los datos de prueba
# Después del entrenamiento, evaluamos el modelo en el conjunto de prueba para ver su rendimiento en datos no vistos.
test_loss, test_acc = model.evaluate(test_images, test_labels)

# Imprimir la precisión (accuracy) en el conjunto de datos de prueba.
print(f"Precisión en los datos de prueba: {test_acc}")

"""
Carga de datos: Se carga el dataset MNIST, que contiene imágenes de dígitos escritos a mano y sus etiquetas correspondientes.
Preprocesamiento: Se ajustan las dimensiones de las imágenes y se normalizan los valores de píxeles.
Construcción del modelo:
Se crean capas convolucionales y de pooling para extraer características espaciales.
Se aplana la salida para preparar el vector de entrada para la capa densa.
Finalmente, una capa densa realiza la clasificación.
Compilación: Se define el optimizador y la función de pérdida.
Entrenamiento: El modelo aprende a partir del conjunto de entrenamiento.
Evaluación: Se evalúa en el conjunto de prueba y se imprime la precisión final.
Este código entrena una red neuronal convolucional básica para clasificar imágenes del conjunto MNIST y es un ejemplo típico de clasificación de imágenes en TensorFlow.
"""