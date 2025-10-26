import socket

# Configuracion del servidor (misma que en servidor.py)
HOST = 'localhost'
PORT = 5000

# Crear un socket TCP para conectarse al servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
    # Conectar al servidor
    socket_servidor.connect( (HOST, PORT) )
    print (f"Conectado al servidor {HOST}:{PORT}")
    while True:
        mensaje = input("Presiona Enter para enviar el mensaje o escribe 'éxito' para terminar: ")
        if not mensaje:
            print("El mensaje no puede estar vacío.")
            continue
        # Enviar mensaje al servidor
        socket_servidor.send( mensaje.encode("utf-8") )
        # Recibir respuesta del servidor
        respuesta = socket_servidor.recv(1024).decode("utf-8")
        if not respuesta:
            print("No se recibió respuesta del servidor.")
            break
        elif respuesta == "Conexión terminada":
            print("Conexion cerrada con exito.")
            break
        else:
            print(f"Respuesta del servidor: {respuesta}")