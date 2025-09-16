import socket
from persistencia import inicializar_db
from persistencia import guardar_mensaje
from datetime import datetime

# Configuracion del servidor
HOST = 'localhost'
PORT = 5000

# Funcion principal para ejecutar el servidor
def ejecutar_servidor():
    # Inicializar el socket del servidor
    socket_servidor = inicializar_socket()
    # Inicializar la base de datos
    inicializar_db()
    if socket_servidor is None: 
        return # Salir si no se pudo inicializar el socket
    print(f"Servidor escuchando en {HOST}:{PORT}")
    try:
        while True:
            # Aceptar una conexion
            conn, addr = socket_servidor.accept()
            with conn:
                # Procesar la conexion del cliente
                procesar_cliente(conn, addr)
    except Exception as e:
        print(f"Error al establecer conexión con el servidor: {e}")
    finally:
        socket_servidor.close()

# Inicializar el socket del servidor
def inicializar_socket():
    try:
        # Se crea Socket TCP como objeto, debido que al utilizar WITH se cierra automaticamente al salir del bloque
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Asociar el socket a la direccion y puerto definidos
        socket_servidor.bind( (HOST, PORT) )
        # Socket en modo escucha
        socket_servidor.listen()
        # Retornar el socket creado
        return socket_servidor
    except OSError as e:
        print(f"Error al iniciar el socket: {e}")
        return None

# Procesar la conexion con el cliente
def procesar_cliente(conn, addr):
    print(f"Conexion establecida desde {addr}")
    while True:
        mensaje = conn.recv(1024).decode("utf-8")
        # Guardar el contenido, la fecha y hora actual, y la IP del cliente en la base de datos
        fecha_evento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if mensaje == "éxito":
            print("Terminando la conexión.")
            respuesta = f"Conexión terminada por el cliente: <{fecha_evento}>"
            conn.send(respuesta.encode("utf-8"))
            break
        try:
            # Guardar el mensaje
            guardar_mensaje(mensaje, fecha_evento, addr[0])
            # Enviar respuesta al cliente
            respuesta = f"Mensaje recibido: <{fecha_evento}>" 
            conn.send(respuesta.encode("utf-8"))
        except Exception as e:
            print(f"Error en la base de datos: {e}")
            conn.send("Error al guardar el mensaje en la base de datos.".encode("utf-8"))

ejecutar_servidor() # Ejecutar el servidor al iniciar el script