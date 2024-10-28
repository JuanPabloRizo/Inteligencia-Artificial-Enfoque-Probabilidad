# HMM simple sin librerías

# Estados ocultos
states = ['Soleado', 'Nublado', 'Lluvioso']

# Observaciones
observations = ['Paraguas', 'Abrigo', 'Sombrero']

# Probabilidad inicial de estar en cada estado oculto
initial_prob = [0.5, 0.3, 0.2]  # P(Soleado), P(Nublado), P(Lluvioso)

# Probabilidades de transición entre estados ocultos
transition_prob = [
    [0.7, 0.2, 0.1],  # Transiciones desde Soleado
    [0.3, 0.4, 0.3],  # Transiciones desde Nublado
    [0.2, 0.3, 0.5]   # Transiciones desde Lluvioso
]

# Probabilidades de emisión (observaciones dadas los estados)
emission_prob = [
    [0.1, 0.4, 0.5],  # P(Paraguas | Soleado), P(Abrigo | Soleado), P(Sombrero | Soleado)
    [0.6, 0.3, 0.1],  # P(Paraguas | Nublado), P(Abrigo | Nublado), P(Sombrero | Nublado)
    [0.7, 0.2, 0.1]   # P(Paraguas | Lluvioso), P(Abrigo | Lluvioso), P(Sombrero | Lluvioso)
]

# Secuencia de observaciones (por ejemplo, viste un paraguas y luego un abrigo)
obs_seq = ['Paraguas', 'Abrigo']

# Algoritmo de Viterbi para encontrar la secuencia de estados más probable
def viterbi(obs_seq, states, initial_prob, transition_prob, emission_prob):
    # Número de observaciones
    n_obs = len(obs_seq)
    # Número de estados
    n_states = len(states)

    # Inicializar la tabla de probabilidades dinámicas
    viterbi_table = [[0] * n_obs for _ in range(n_states)]
    # Inicializar la tabla para guardar el camino más probable
    path_table = [[0] * n_obs for _ in range(n_states)]

    # Inicialización (paso base)
    for s in range(n_states):
        viterbi_table[s][0] = initial_prob[s] * emission_prob[s][observations.index(obs_seq[0])]
        path_table[s][0] = 0

    # Recursión (paso recursivo)
    for t in range(1, n_obs):
        for s in range(n_states):
            max_prob = max(viterbi_table[s_prev][t-1] * transition_prob[s_prev][s] for s_prev in range(n_states))
            viterbi_table[s][t] = max_prob * emission_prob[s][observations.index(obs_seq[t])]
            # Guardar el estado anterior con la máxima probabilidad
            path_table[s][t] = max(range(n_states), key=lambda s_prev: viterbi_table[s_prev][t-1] * transition_prob[s_prev][s])

    # Terminar el algoritmo (obtener el mejor camino)
    # Encontrar el estado con la máxima probabilidad en la última observación
    last_state = max(range(n_states), key=lambda s: viterbi_table[s][-1])

    # Reconstruir el camino más probable
    best_path = [last_state]
    for t in range(n_obs - 1, 0, -1):
        last_state = path_table[last_state][t]
        best_path.insert(0, last_state)

    # Traducir el camino de índices a nombres de estados
    best_state_path = [states[i] for i in best_path]

    return best_state_path

# Ejecutar el algoritmo Viterbi
result = viterbi(obs_seq, states, initial_prob, transition_prob, emission_prob)
print("Secuencia más probable de estados ocultos:")
print(result)
"""
Definición del modelo:

states: Los posibles estados ocultos del modelo (Soleado, Nublado, Lluvioso).
observations: Las posibles observaciones (Paraguas, Abrigo, Sombrero).
initial_prob: La probabilidad inicial de estar en cada uno de los estados al inicio del proceso.
transition_prob: Matriz de transición que define la probabilidad de moverse de un estado oculto a otro.
emission_prob: Matriz de emisión que define la probabilidad de observar una cierta señal (paraguas, abrigo, etc.) dado un estado oculto.
Algoritmo de Viterbi:

Calcula la secuencia más probable de estados ocultos dado una secuencia observada usando programación dinámica.
Se utiliza una tabla (viterbi_table) para almacenar las probabilidades máximas acumuladas hasta cada observación.
Otra tabla (path_table) guarda el estado previo más probable que llevó a la observación actual, lo cual permite reconstruir el mejor camino al final.
Salida:

La secuencia más probable de estados ocultos que genera la secuencia observada.
"""