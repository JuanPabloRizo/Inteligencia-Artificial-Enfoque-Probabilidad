# Importar bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC  # SVM con núcleos
from sklearn.model_selection import train_test_split

# Cargar un conjunto de datos de ejemplo (Iris)
iris = datasets.load_iris()
X = iris.data[:, :2]  # Tomar solo las dos primeras características para visualización
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo SVM con un núcleo radial (RBF)
svm_model = SVC(kernel='rbf', gamma='scale')  # gamma='scale' es un ajuste automático

# Entrenar el modelo
svm_model.fit(X_train, y_train)

# Hacer predicciones
predictions = svm_model.predict(X_test)

# Visualizar los resultados
def plot_decision_boundary(svm_model, X, y):
    # Establecer límites del gráfico
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    # Predecir en el espacio de decisión
    Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Dibujar el contorno y los puntos de entrenamiento
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', cmap=plt.cm.coolwarm)
    plt.title('Máquinas de Vectores Soporte (SVM) con Núcleo RBF')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.show()

# Llamar a la función de visualización
plot_decision_boundary(svm_model, X, y)
"""
Importación de bibliotecas:

numpy: Se utiliza para operaciones matemáticas y manipulación de arrays.
matplotlib.pyplot: Se usa para visualizar datos y resultados.
sklearn.datasets: Para cargar conjuntos de datos de ejemplo.
sklearn.svm: Contiene el modelo SVC que implementa SVM con núcleos.
sklearn.model_selection: Para dividir el conjunto de datos en entrenamiento y prueba.
Cargar el conjunto de datos:

Se carga el conjunto de datos de Iris y se seleccionan solo las dos primeras características para facilitar la visualización.
División del conjunto de datos:

Se divide el conjunto de datos en entrenamiento (70%) y prueba (30%) para evaluar el modelo después de entrenarlo.
Creación y entrenamiento del modelo:

Se crea un modelo SVM con un núcleo radial (RBF) y se ajusta el modelo a los datos de entrenamiento.
Predicciones:

Se utilizan los datos de prueba para hacer predicciones.
Visualización:

Se define una función plot_decision_boundary para visualizar el espacio de decisión 
generado por el modelo SVM. Esta función crea una cuadrícula de puntos y predice su clase, trazando el contorno de decisión y los puntos de datos.
"""