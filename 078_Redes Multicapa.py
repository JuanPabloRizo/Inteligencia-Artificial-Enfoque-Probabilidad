import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesamiento de los datos
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Construcción del modelo de red neuronal multicapa
model = models.Sequential()

# Capa de entrada
model.add(layers.Input(shape=(28, 28, 1)))  # Capa de entrada para imágenes 28x28 con un canal

# Primera capa oculta con 128 neuronas y función de activación ReLU
model.add(layers.Flatten())  # Aplana la imagen 2D a un vector 1D
model.add(layers.Dense(128, activation='relu'))  # Capa densa totalmente conectada

# Capa de salida con 10 neuronas (una para cada dígito) y activación softmax
model.add(layers.Dense(10, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5, batch_size=64)

# Evaluar el modelo en los datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)

print(f"Precisión en los datos de prueba: {test_acc}")

"""
Importación de Bibliotecas:

Importamos TensorFlow y Keras para construir y entrenar la red.
Carga de Datos:

Cargamos el conjunto de datos MNIST, que contiene imágenes de dígitos del 0 al 9.
Preprocesamiento:

Redimensionamos las imágenes para que tengan forma (28, 28, 1) (altura, ancho, canales) y normalizamos los valores a un rango de 0 a 1 dividiendo por 255.
Construcción del Modelo:

Usamos un modelo secuencial de Keras para construir nuestra red.
Capa de Entrada: Definimos la forma de entrada de las imágenes.
Primera Capa Oculta: Añadimos una capa densa con 128 neuronas y la función de activación ReLU.
Capa de Salida: Añadimos una capa densa con 10 neuronas y la función de activación softmax para clasificar los dígitos.
Compilación del Modelo:

Compilamos el modelo con el optimizador Adam, la función de pérdida de entropía cruzada y la métrica de precisión.
Entrenamiento del Modelo:

Entrenamos el modelo utilizando los datos de entrenamiento durante 5 épocas con un tamaño de lote de 64.
Evaluación del Modelo:

Evaluamos el modelo utilizando los datos de prueba y mostramos la precisión obtenida.
"""