# Definir las probabilidades
P_Spam = 0.4  # Probabilidad de que un correo sea spam
P_No_Spam = 0.6  # Probabilidad de que un correo no sea spam

# Probabilidades condicionales de las palabras dado Spam y No Spam
P_gratis_given_spam = 0.7
P_gratis_given_no_spam = 0.1
P_dinero_given_spam = 0.6
P_dinero_given_no_spam = 0.2
P_oferta_given_spam = 0.8
P_oferta_given_no_spam = 0.1

# El correo contiene las palabras 'gratis' y 'dinero'
palabras_en_correo = ['gratis', 'dinero']

# Calcular la probabilidad de que el correo sea Spam y No Spam
# Usamos la suposición de independencia (Naïve)

# Para Spam
P_correo_given_spam = P_gratis_given_spam * P_dinero_given_spam
P_posterior_spam = P_correo_given_spam * P_Spam

# Para No Spam
P_correo_given_no_spam = P_gratis_given_no_spam * P_dinero_given_no_spam
P_posterior_no_spam = P_correo_given_no_spam * P_No_Spam

# Normalización (opcional, para que sumen a 1)
P_total = P_posterior_spam + P_posterior_no_spam
P_posterior_spam_normalizado = P_posterior_spam / P_total
P_posterior_no_spam_normalizado = P_posterior_no_spam / P_total

# Imprimir el resultado
print(f"Probabilidad de Spam: {P_posterior_spam_normalizado:.2f}")
print(f"Probabilidad de No Spam: {P_posterior_no_spam_normalizado:.2f}")

# Clasificación final
if P_posterior_spam_normalizado > P_posterior_no_spam_normalizado:
    print("El correo es clasificado como: Spam")
else:
    print("El correo es clasificado como: No Spam")

"""
Definición de Probabilidades:
Primero, definimos las probabilidades previas P(Spam) y P(No Spam), 
así como las probabilidades condicionales de que ciertas palabras estén 
presentes dado que el correo es spam o no.
Calculo de P(correo∣Spam) y P(correo∣No Spam):
Usamos la suposición de independencia (Naïve) para calcular la probabilidad
de que el correo contenga las palabras "gratis" y "dinero" bajo la clase spam y no spam.
Cálculo de la Posterior:
Aplicamos el teorema de Bayes para obtener la probabilidad posterior de que
el correo sea spam o no spam. Esto se realiza multiplicando la probabilidad 
condicional por la probabilidad previa.
Normalización:
Para que las probabilidades sumen a 1, normalizamos dividiendo por la suma 
de las probabilidades calculadas (opcional pero útil para la interpretación).
Clasificación Final:
Comparamos las probabilidades de spam y no spam y clasificamos el correo en consecuencia.
"""