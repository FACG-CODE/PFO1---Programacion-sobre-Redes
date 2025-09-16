import sqlite3

# Función para inicializar la base de datos y crear la tabla si no existe
def inicializar_db():
    # Crear una conexion a la base de datos SQLite y creamos un cursor para ejecutar comandos SQL
    conn = sqlite3.connect("persistencia.db")
    try:
        cursor = conn.cursor()
        # Creamos la tabla para almacenar los mensajes
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS mensajes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contenido TEXT NOT NULL,
                    fecha_envio TEXT NOT NULL,
                    ip_cliente TEXT NOT NULL
                    )
                    ''')
        # Confirmamos los cambios y cerramos la conexion
        conn.commit()
        print("Base de datos inicializada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

# Función para guardar un mensaje en la base de datos
def guardar_mensaje(contenido, fecha_envio, ip_cliente):
    # Crear una conexion a la base de datos SQLite y creamos un cursor para ejecutar comandos SQL
    conn = sqlite3.connect("persistencia.db")
    try: 
        cursor = conn.cursor()
        # Insertar el mensaje en la tabla
        cursor.execute('''
                    INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) 
                    VALUES (?, ?, ?)''', (contenido, fecha_envio, ip_cliente))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje: {e}")
    finally:
        if conn:
            conn.close()