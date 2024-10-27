import numpy as np  # Importa la biblioteca numpy para operaciones numéricas
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.linear_model import LogisticRegression  # Importa el modelo de regresión logística
from sklearn.metrics import accuracy_score  # Para evaluar la precisión del modelo

# Generar datos sintéticos
# X son las características (dos variables), y son las etiquetas (0 o 1)
np.random.seed(0)  # Establece la semilla para la reproducibilidad
X = np.random.rand(100, 2)  # Genera 100 ejemplos con 2 características aleatorias entre 0 y 1
# La etiqueta y es 1 si la suma de las características es mayor que 1, de lo contrario es 0
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Crea etiquetas binarias (0 o 1) basadas en la condición

# Dividir el conjunto de datos en entrenamiento y prueba
# train_test_split divide los datos en dos conjuntos, uno para entrenar el modelo y otro para evaluarlo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2 indica que el 20% de los datos se utilizarán para prueba
# random_state=42 asegura que la división sea reproducible

# Crear el modelo de regresión logística
model = LogisticRegression()  # Inicializa el modelo de regresión logística

# Entrenar el modelo
model.fit(X_train, y_train)  # Ajusta el modelo a los datos de entrenamiento

# Hacer predicciones
y_pred = model.predict(X_test)  # Realiza predicciones sobre el conjunto de prueba

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)  # Calcula la precisión comparando las predicciones con las etiquetas reales
print(f"Precisión del modelo: {accuracy:.2f}")  # Muestra la precisión del modelo en formato de 2 decimales

# Mostrar las probabilidades de predicción
probabilities = model.predict_proba(X_test)  # Obtiene las probabilidades de pertenencia a cada clase
print("Probabilidades de las predicciones:")
print(probabilities)  # Muestra las probabilidades de cada predicción
