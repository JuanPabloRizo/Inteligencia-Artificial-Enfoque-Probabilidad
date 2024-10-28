import numpy as np

# Paso 1: Inicialización de parámetros
# p_A y p_B son las probabilidades iniciales de que las monedas A y B saquen "cara"
p_A = 0.6  # Probabilidad inicial de que la moneda A salga cara
p_B = 0.5  # Probabilidad inicial de que la moneda B salga cara

# Datos: Resultados observados (1 = cara, 0 = cruz) de los lanzamientos (cada sublista es un experimento)
observaciones = np.array([[1, 0, 1, 1, 0],   # experimento 1
                          [1, 1, 0, 1, 1],   # experimento 2
                          [0, 1, 1, 0, 0],   # experimento 3
                          [1, 1, 1, 1, 0]])  # experimento 4

# Función auxiliar para calcular la verosimilitud
def calcular_verosimilitud(p, datos):
    return p**np.sum(datos) * (1 - p)**(len(datos) - np.sum(datos))

# Paso 2: Algoritmo EM
for iteracion in range(10):  # 10 iteraciones del algoritmo EM
    # Paso E: Expectativa
    # Para cada experimento, calcular las probabilidades de que los resultados sean generados por la moneda A o B
    pesos_A = np.zeros(len(observaciones))  # Para almacenar las probabilidades de que cada experimento use la moneda A
    pesos_B = np.zeros(len(observaciones))  # Para almacenar las probabilidades de que cada experimento use la moneda B
    
    for i, experimento in enumerate(observaciones):
        # Calcular la probabilidad de que los resultados hayan sido generados por A y B
        verosimilitud_A = calcular_verosimilitud(p_A, experimento)
        verosimilitud_B = calcular_verosimilitud(p_B, experimento)
        
        # Normalizar las probabilidades para que sumen 1
        peso_A = verosimilitud_A / (verosimilitud_A + verosimilitud_B)
        peso_B = verosimilitud_B / (verosimilitud_A + verosimilitud_B)
        
        pesos_A[i] = peso_A
        pesos_B[i] = peso_B
    
    # Paso M: Maximización
    # Recalcular p_A y p_B usando las expectativas calculadas en el paso E
    p_A = np.sum(pesos_A * np.sum(observaciones, axis=1)) / np.sum(pesos_A * len(observaciones[0]))
    p_B = np.sum(pesos_B * np.sum(observaciones, axis=1)) / np.sum(pesos_B * len(observaciones[0]))
    
    # Imprimir los valores actuales de p_A y p_B en cada iteración
    print(f"Iteración {iteracion + 1}: p_A = {p_A:.3f}, p_B = {p_B:.3f}")

# Resultado final
print(f"Probabilidad final estimada para la moneda A: {p_A:.3f}")
print(f"Probabilidad final estimada para la moneda B: {p_B:.3f}")

"""
Inicialización:
Se inicializan las probabilidades de que las monedas A y B salgan cara, 
PA y PB.
Datos:
Tenemos un conjunto de observaciones que consisten en varios lanzamientos 
de monedas, donde cada sublista representa los resultados de un experimento (1 = cara, 0 = cruz).
Función de Verosimilitud:
La función calcular_verosimilitud(p, datos) calcula la probabilidad de que un conjunto 
de datos sea generado por una moneda con probabilidad p de sacar cara.
Iteraciones del Algoritmo EM:
Para cada experimento, calculamos las probabilidades de que los resultados observados 
sean generados por la moneda A o B (Paso E).
Luego, actualizamos las probabilidades PA y PB
​en función de las expectativas calculadas (Paso M).
Resultados:
El algoritmo imprime los valores actualizados de 
PA y PBen cada iteración, mostrando cómo convergen hacia las 
probabilidades estimadas finales.
"""