# Importar las bibliotecas necesarias
import numpy as np
from sklearn.datasets import load_iris  # Para cargar el conjunto de datos Iris
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.neighbors import KNeighborsClassifier  # Para el clasificador K-NN
from sklearn.metrics import accuracy_score  # Para calcular la precisión del modelo

# Cargar el conjunto de datos Iris
# 'load_iris()' devuelve un objeto con atributos que contienen las características y las etiquetas
iris = load_iris()
X = iris.data  # Extraer las características (longitud y ancho de sépalos y pétalos)
y = iris.target  # Extraer las clases (tipos de iris: setosa, versicolor, virginica)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
# 'test_size=0.2' indica que el 20% de los datos se utilizarán para pruebas
# 'random_state=42' garantiza que la división sea reproducible
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador K-NN
# 'n_neighbors=3' significa que se considerarán 3 vecinos más cercanos para la clasificación
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador con los datos de entrenamiento
# 'fit()' toma los datos de características (X_train) y las etiquetas correspondientes (y_train) 
# para ajustar el modelo K-NN
knn.fit(X_train, y_train)

# Hacer predicciones en los datos de prueba
# 'predict()' utiliza el modelo entrenado para clasificar las características en X_test
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo
# 'accuracy_score()' compara las etiquetas predichas (y_pred) con las etiquetas reales (y_test)
# y devuelve la proporción de predicciones correctas
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
# La precisión se imprime como un porcentaje con dos decimales
print(f"Precisión del modelo: {accuracy:.2f}")

"""
Cargar Datos:

Usamos el conjunto de datos Iris, que es un clásico en la clasificación de patrones. Contiene medidas de diferentes tipos de flores de iris.
División de Datos:

Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.
Clasificador K-NN:

Se crea un clasificador K-Vecinos más Cercanos (K-NN), que es un algoritmo de aprendizaje supervisado utilizado para clasificación y regresión.
Entrenamiento:

El modelo se entrena con los datos de entrenamiento usando el método fit().
Predicciones:

Se hacen predicciones sobre el conjunto de prueba y se evalúa la precisión usando accuracy_score().
Salida:

Imprimimos la precisión del modelo, que indica cuán bien el modelo ha clasificado los datos de prueba.
"""