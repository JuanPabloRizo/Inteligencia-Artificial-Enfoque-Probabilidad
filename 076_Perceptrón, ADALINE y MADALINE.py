import numpy as np  # Importamos la librería NumPy para operaciones numéricas

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        # Inicializamos la tasa de aprendizaje y el número de iteraciones
        self.learning_rate = learning_rate  # Tasa de aprendizaje que afecta cuánto se actualizan los pesos
        self.n_iters = n_iters  # Número de iteraciones para el entrenamiento
        self.weights = None  # Inicializamos los pesos a None
        self.bias = None  # Inicializamos el bias a None

    def fit(self, X, y):
        # Método para entrenar el perceptrón
        n_samples, n_features = X.shape  # Obtenemos el número de muestras y características
        self.weights = np.zeros(n_features)  # Inicializamos los pesos con ceros
        self.bias = 0  # Inicializamos el bias con cero

        # Algoritmo de aprendizaje
        for _ in range(self.n_iters):  # Repetimos el entrenamiento n_iters veces
            for idx, x_i in enumerate(X):  # Iteramos sobre cada muestra
                linear_output = np.dot(x_i, self.weights) + self.bias  # Calculamos la salida lineal
                y_predicted = self.activation_function(linear_output)  # Aplicamos la función de activación
                # Actualizar los pesos y el bias
                update = self.learning_rate * (y[idx] - y_predicted)  # Calculamos la actualización
                self.weights += update * x_i  # Actualizamos los pesos
                self.bias += update  # Actualizamos el bias

    def activation_function(self, x):
        # Función de activación escalón
        return np.where(x >= 0, 1, 0)  # Retorna 1 si x es mayor o igual a 0, de lo contrario retorna 0

    def predict(self, X):
        # Método para hacer predicciones
        linear_output = np.dot(X, self.weights) + self.bias  # Calculamos la salida lineal
        y_predicted = self.activation_function(linear_output)  # Aplicamos la función de activación
        return y_predicted  # Retornamos las predicciones

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de entrenamiento (AND lógico)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
    y = np.array([0, 0, 0, 1])  # Etiquetas de salida

    perceptron = Perceptron(learning_rate=0.1, n_iters=10)  # Creamos una instancia del Perceptrón
    perceptron.fit(X, y)  # Entrenamos el modelo con los datos
    predictions = perceptron.predict(X)  # Hacemos predicciones con los datos de entrada

    print("Predicciones:", predictions)  # Debería predecir [0, 0, 0, 1]
"""
Inicialización: Se definen la tasa de aprendizaje y el número de iteraciones.
Ajuste (fit): Se inicializan los pesos y el bias. Se itera sobre las muestras y se actualizan los pesos y el bias basándose en el error.
Función de activación: Se usa una función escalón para clasificar las entradas.
Predicción: Se realiza la predicción multiplicando las entradas por los pesos y sumando el bias.
"""