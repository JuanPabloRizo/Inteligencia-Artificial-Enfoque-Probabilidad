# Definir las probabilidades
P_Spam = 0.4  # Probabilidad de que un correo sea spam
P_No_Spam = 0.6  # Probabilidad de que un correo no sea spam

# Probabilidades condicionales
P_oferta_given_spam = 0.8  # P("oferta" | Spam)
P_oferta_given_no_spam = 0.1  # P("oferta" | No Spam)

# Calcular P("oferta") utilizando la ley de la probabilidad total
P_oferta = (P_oferta_given_spam * P_Spam) + (P_oferta_given_no_spam * P_No_Spam)

# Aplicar el teorema de Bayes para calcular P(Spam | "oferta")
P_Spam_given_oferta = (P_oferta_given_spam * P_Spam) / P_oferta

# Imprimir el resultado
print(f"La probabilidad de que un correo sea spam dado que contiene 'oferta' es: {P_Spam_given_oferta:.2f}")
