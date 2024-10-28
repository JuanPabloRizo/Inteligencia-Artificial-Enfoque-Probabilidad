import random

class PCFG:
    def __init__(self):
        # Define la gramática con probabilidades para cada producción.
        # Cada no terminal tiene una lista de producciones en la forma (producción, probabilidad).
        self.grammar = {
            'S': [('NP', 'VP', 0.9),  # La producción S -> NP VP tiene una probabilidad de 0.9
                  ('VP', '', 0.1)],  # La producción S -> VP tiene una probabilidad de 0.1
            'NP': [('Det', 'N', 0.5),  # La producción NP -> Det N tiene una probabilidad de 0.5
                   ('NP', 'PP', 0.5)],  # La producción NP -> NP PP tiene una probabilidad de 0.5
            'VP': [('V', 'NP', 0.5),  # La producción VP -> V NP tiene una probabilidad de 0.5
                   ('V', '', 0.5)],  # La producción VP -> V tiene una probabilidad de 0.5
            'Det': [('el', 0.6),  # La producción Det -> 'el' tiene una probabilidad de 0.6
                    ('la', 0.4)],  # La producción Det -> 'la' tiene una probabilidad de 0.4
            'N': [('perro', 0.3),  # La producción N -> 'perro' tiene una probabilidad de 0.3
                  ('gato', 0.7)],  # La producción N -> 'gato' tiene una probabilidad de 0.7
            'V': [('come', 0.5),  # La producción V -> 'come' tiene una probabilidad de 0.5
                  ('ladra', 0.5)],  # La producción V -> 'ladra' tiene una probabilidad de 0.5
            'PP': [('P', 'NP', 1.0)],  # La producción PP -> P NP tiene una probabilidad de 1.0
            'P': [('con', 1.0)]  # La producción P -> 'con' tiene una probabilidad de 1.0
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
pcfg = PCFG()  # Crea una instancia de la gramática.
for _ in range(5):  # Genera 5 oraciones.
    print(pcfg.generate())  # Imprime las oraciones generadas.
"""
Definición de la Gramática: Se define una gramática probabilística donde cada no terminal tiene una lista de producciones con sus respectivas probabilidades.

Generación de Cadenas:

La función generate expande un símbolo inicial.
Se selecciona una producción basada en su probabilidad.
Si el símbolo es terminal, se retorna tal cual.
Ejemplo de Uso: Se crea una instancia de PCFG y se generan varias oraciones, imprimiéndolas en la consola.
"""