import random

class LexicalizedPCFG:
    def __init__(self):
        # Define la gramática con probabilidades para producciones lexicalizadas.
        self.grammar = {
            'S': [
                ('NP', 'VP', 0.9),  # S -> NP VP
                ('VP', '', 0.1)     # S -> VP
            ],
            'NP': [
                ('Det', 'N', 0.5),  # NP -> Det N
                ('NP', 'PP', 0.5)   # NP -> NP PP
            ],
            'VP': [
                ('V', 'NP', 0.5),   # VP -> V NP
                ('V', '', 0.5)      # VP -> V
            ],
            'PP': [
                ('P', 'NP', 1.0)    # PP -> P NP
            ],
            'Det': [
                ('el', 0.6),        # Det -> 'el'
                ('la', 0.4)         # Det -> 'la'
            ],
            'N': [
                ('perro', 0.3),     # N -> 'perro'
                ('gato', 0.7)       # N -> 'gato'
            ],
            'V': [
                ('come', 0.5),      # V -> 'come'
                ('ladra', 0.5)      # V -> 'ladra'
            ],
            'P': [
                ('con', 1.0)        # P -> 'con'
            ]
        }

    def generate(self, symbol='S'):
        """
        Genera una cadena a partir del símbolo inicial.

        :param symbol: El símbolo actual a expandir (inicialmente es 'S').
        :return: Cadena generada.
        """
        # Si el símbolo es terminal (no está en la gramática), lo retorna tal cual.
        if symbol not in self.grammar:
            return symbol  # Retorna el símbolo como es.

        # Selecciona una producción basada en sus probabilidades
        productions = self.grammar[symbol]  # Obtiene las producciones del símbolo actual.
        total_prob = sum(prob for *_, prob in productions)  # Suma las probabilidades de todas las producciones.
        random_value = random.uniform(0, total_prob)  # Genera un número aleatorio entre 0 y total_prob.

        cumulative_prob = 0.0  # Inicializa la probabilidad acumulada a 0.
        for production in productions:  # Recorre todas las producciones del símbolo.
            *rule, prob = production  # Descompone la producción en la regla y la probabilidad.
            cumulative_prob += prob  # Aumenta la probabilidad acumulada con la probabilidad de la producción.
            if random_value < cumulative_prob:  # Si el valor aleatorio está dentro del rango acumulado:
                # Expande la regla elegida
                # Llama recursivamente a 'generate' para cada símbolo en la regla y une los resultados en una cadena.
                return ' '.join(self.generate(s) for s in rule)

# Ejemplo de uso
lpcfg = LexicalizedPCFG()  # Crea una instancia de la gramática.
for _ in range(5):  # Genera 5 oraciones.
    print(lpcfg.generate())  # Imprime las oraciones generadas.
"""
Importación de Módulos:

import random: Se importa el módulo random para generar números aleatorios.
Definición de la Clase LexicalizedPCFG:

Define la clase que contendrá la gramática lexicalizada.
Método Constructor __init__:

Inicializa la clase y define la gramática con producciones y probabilidades. Cada regla incluye palabras específicas, lo que permite modelar la estructura del lenguaje de manera más precisa.
Método generate:

Similar al de la PCFG, este método genera una cadena a partir de un símbolo inicial, utilizando probabilidades para seleccionar producciones.
Ejemplo de Uso:

Se crea una instancia de la gramática y se generan cinco oraciones, que se imprimen en la consola.
"""