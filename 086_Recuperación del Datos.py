# Importar el módulo sqlite3 para interactuar con bases de datos SQLite
import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('ejemplo.db')  # 'ejemplo.db' es el nombre del archivo de la base de datos
cursor = conn.cursor()  # Crear un objeto cursor que permite ejecutar comandos SQL

# Crear una tabla llamada 'personas' si no existe
# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')
# Columna 'id', tipo INTEGER, autoincremental y clave primaria
# Columna 'nombre', tipo TEXT y no nula
# Columna 'edad', tipo INTEGER y no nula

# Insertar datos en la tabla 'personas'
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Alice', 30)")  # Inserta a Alice, 30 años
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Bob', 25)")     # Inserta a Bob, 25 años
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Charlie', 35)") # Inserta a Charlie, 35 años

# Confirmar los cambios en la base de datos
conn.commit()  # Guarda todos los cambios realizados en la base de datos

# Recuperar datos de la tabla 'personas'
cursor.execute("SELECT * FROM personas")  # Ejecuta una consulta SQL para seleccionar todas las filas
resultados = cursor.fetchall()  # Recupera todos los registros y los almacena en una lista

# Imprimir los resultados recuperados
print("Datos recuperados:")  # Mensaje indicativo
for fila in resultados:  # Iterar sobre cada fila de resultados
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")  # Imprime el ID, nombre y edad de cada persona

# Cerrar la conexión a la base de datos
conn.close()  # Cierra la conexión, liberando recursos asociados a la misma

"""
Importación del Módulo sqlite3:

Este módulo se utiliza para interactuar con bases de datos SQLite.
Conexión a la Base de Datos:

Se establece una conexión con la base de datos ejemplo.db. Si el archivo no existe, se crea uno nuevo.
Creación de una Tabla:

Se ejecuta una instrucción SQL para crear una tabla llamada personas si no existe. Esta tabla tiene tres columnas: id, nombre, y edad.
Inserción de Datos:

Se insertan tres registros en la tabla personas.
Confirmación de Cambios:

Se confirma la transacción utilizando conn.commit() para asegurar que los cambios se guarden en la base de datos.
Recuperación de Datos:

Se ejecuta una consulta SQL para recuperar todos los registros de la tabla personas.
Impresión de Resultados:

Se recorren y se imprimen los resultados recuperados.
Cierre de la Conexión:

Finalmente, se cierra la conexión con la base de datos para liberar recursos.
"""