import numpy as np
import random

class FiltradoDeParticulas:
    def __init__(self, num_particulas, rango_estado):
        """
        Inicialización del Filtro de Partículas.
        
        Parámetros:
        num_particulas - Número de partículas que se usarán.
        rango_estado - Rango de valores posibles para el estado (posición).
        """
        self.num_particulas = num_particulas
        self.particulas = np.random.uniform(rango_estado[0], rango_estado[1], num_particulas)  # Posición inicial de las partículas
        self.pesos = np.ones(num_particulas) / num_particulas  # Inicialización de los pesos

    def prediccion(self, movimiento, ruido_proceso):
        """
        Predicción del siguiente estado de cada partícula.
        
        Parámetros:
        movimiento - Movimiento esperado del objeto (cambio de posición).
        ruido_proceso - Ruido asociado al proceso.
        """
        self.particulas += movimiento + np.random.normal(0, ruido_proceso, self.num_particulas)  # Se añade ruido al movimiento

    def actualizacion(self, medicion, ruido_medicion):
        """
        Actualización de los pesos de las partículas en base a la nueva medición.
        
        Parámetros:
        medicion - Nueva medición observada.
        ruido_medicion - Ruido asociado a la medición.
        """
        # Calcular la probabilidad de cada partícula dado la medición
        for i in range(self.num_particulas):
            self.pesos[i] = self.gaussiana(medicion, self.particulas[i], ruido_medicion)

        # Normalizar los pesos para que sumen a 1
        self.pesos += 1.e-300  # Evitar errores de división por cero
        self.pesos /= sum(self.pesos)

    def remuestreo(self):
        """
        Seleccionar partículas en base a sus pesos.
        """
        indices = np.random.choice(range(self.num_particulas), self.num_particulas, p=self.pesos)
        self.particulas = self.particulas[indices]
        self.pesos = np.ones(self.num_particulas) / self.num_particulas  # Restablecer pesos uniformemente

    def estimacion(self):
        """
        Estimación del estado actual basado en las partículas.
        """
        return np.mean(self.particulas)

    def gaussiana(self, mu, x, sigma):
        """
        Calcular la probabilidad de la medición usando una distribución gaussiana.
        
        Parámetros:
        mu - Media de la distribución.
        x - Valor en el cual se evalúa.
        sigma - Desviación estándar de la distribución.
        """
        return (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(- (x - mu)**2 / (2 * sigma**2))

# Parámetros del sistema
num_particulas = 1000
rango_estado = (0, 100)  # Rango de la posición inicial del objeto
movimiento = 1.0         # Movimiento del objeto (velocidad constante)
ruido_proceso = 0.2      # Ruido en el movimiento
ruido_medicion = 2.0     # Ruido en las mediciones

# Inicializar el filtro de partículas
filtro = FiltradoDeParticulas(num_particulas, rango_estado)

# Simulación de un objeto en movimiento con mediciones ruidosas
mediciones_reales = [i + np.random.normal(0, ruido_medicion) for i in range(20)]
estimaciones = []

for medicion in mediciones_reales:
    filtro.prediccion(movimiento, ruido_proceso)  # Predicción de la posición
    filtro.actualizacion(medicion, ruido_medicion)  # Actualización con la nueva medición
    filtro.remuestreo()  # Remuestreo de partículas
    estimacion_actual = filtro.estimacion()  # Estimación actual del estado
    estimaciones.append(estimacion_actual)

    print(f"Medición: {medicion:.2f}, Estimación: {estimacion_actual:.2f}")

# Imprimir las estimaciones finales
print("\nEstimaciones finales de la posición:", estimaciones)
"""
Inicialización:
Creamos N partículas distribuidas uniformemente en un rango de posibles posiciones iniciales.
Los pesos iniciales de todas las partículas se asignan uniformemente.
Predicción:
Para cada partícula, se realiza una predicción del siguiente estado, agregando el movimiento 
esperado del objeto más un ruido que simula las incertidumbres del proceso.
Actualización:
Se recibe una nueva medición del sistema, y se ajustan los pesos de las partículas en función 
de qué tan probable es que esa partícula esté en el estado que generó la medición. Para ello, 
se utiliza una función de densidad gaussiana para modelar el error en la medición.
Remuestreo:
Se seleccionan partículas nuevas basadas en sus pesos. Aquellas partículas con mayor peso 
tienen más probabilidad de ser seleccionadas, lo que ayuda a concentrarse en las regiones 
más probables del espacio de estados.
Estimación:
La estimación del estado actual se calcula como el promedio de todas las partículas, 
lo que proporciona una aproximación a la distribución posterior.
Salida esperada:
El código imprimirá las mediciones ruidosas simuladas y las estimaciones 
de la posición del objeto generadas por el filtrado de partículas.
"""