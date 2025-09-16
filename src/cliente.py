import socket

# Configuracion del servidor (misma que en servidor.py)
HOST = 'localhost'
PORT = 5000

# Mensajes a enviar
mensajes = [
    "Hola, ¿cómo estás?",
    "¿Qué estás haciendo?",
    "¿Cuál es tu color favorito?",
    "¿Te gusta programar?",
    "éxito"  # Mensaje para indicar al servidor que cierre la conexión
]

# Crear un socket TCP para conectarse al servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
    # Conectar al servidor
    socket_servidor.connect( (HOST, PORT) )
    print (f"Conectado al servidor {HOST}:{PORT}")
    for mensaje in mensajes:
        # Enviar mensaje al servidor
        socket_servidor.send( mensaje.encode("utf-8") )
        # Recibir respuesta del servidor
        respuesta = socket_servidor.recv(1024).decode("utf-8")
        if not respuesta:
            print("No se recibió respuesta del servidor.")
            break
        print(f"Respuesta del servidor: {respuesta}")