# Importar el módulo sqlite3 para interactuar con bases de datos SQLite
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('ejemplo.db')  # 'ejemplo.db' es el nombre del archivo de la base de datos
cursor = conn.cursor()  # Crear un objeto cursor que permite ejecutar comandos SQL

# Supongamos que ya hay una tabla 'personas' con datos en la base de datos.
# Aquí vamos a extraer información específica de esa tabla.

# Recuperar nombres de personas mayores de 30 años
edad_minima = 30  # Definimos la edad mínima para la búsqueda
cursor.execute("SELECT nombre FROM personas WHERE edad > ?", (edad_minima,))  # Consulta para obtener nombres
resultados = cursor.fetchall()  # Recuperar todos los resultados de la consulta

# Imprimir los nombres recuperados
print(f"Nombres de personas mayores de {edad_minima} años:")
for fila in resultados:  # Iterar sobre cada fila de resultados
    print(f"Nombre: {fila[0]}")  # Imprime el nombre de cada persona

# Recuperar la cantidad total de personas en la base de datos
cursor.execute("SELECT COUNT(*) FROM personas")  # Consulta para contar todas las personas
total_personas = cursor.fetchone()[0]  # Recupera el resultado de la consulta (un único valor)

# Imprimir la cantidad total de personas
print(f"\nTotal de personas en la base de datos: {total_personas}")

# Cerrar la conexión a la base de datos
conn.close()  # Cierra la conexión, liberando recursos asociados a la misma

"""
Importar el Módulo sqlite3:

import sqlite3 permite trabajar con SQLite, un sistema de gestión de bases de datos muy usado en aplicaciones ligeras.
Conexión a la Base de Datos:

conn = sqlite3.connect('ejemplo.db'): Abre una conexión con la base de datos ejemplo.db. Si no existe, se crea.
Crear un Cursor:

cursor = conn.cursor(): Crea un cursor que se usa para ejecutar comandos SQL y recuperar resultados.
Recuperar Nombres de Personas Mayores de 30 Años:

edad_minima = 30: Establece una variable que define la edad mínima para filtrar.
cursor.execute(...): Ejecuta una consulta SQL que selecciona los nombres de las personas cuya edad es mayor que edad_minima.
? es un marcador de posición que ayuda a prevenir inyecciones SQL. Los valores se pasan como una tupla (edad_minima,).
resultados = cursor.fetchall(): Recupera todas las filas resultantes de la consulta.
Imprimir Nombres Recuperados:

print(...): Muestra un mensaje informando que se listarán los nombres.
for fila in resultados:: Itera sobre cada fila recuperada.
print(f"Nombre: {fila[0]}"): Imprime el nombre de cada persona.
Contar el Total de Personas:

cursor.execute("SELECT COUNT(*) FROM personas"): Ejecuta una consulta SQL que cuenta el número total de personas en la tabla personas.
total_personas = cursor.fetchone()[0]: Recupera el único valor devuelto (el total de personas).
Imprimir Total de Personas:

print(f"\nTotal de personas en la base de datos: {total_personas}"): Muestra el total de personas en la base de datos.
Cerrar la Conexión:

conn.close(): Cierra la conexión a la base de datos para liberar recursos. Siempre es buena práctica cerrar las conexiones cuando ya no se necesitan.
"""