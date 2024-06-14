# Servidor de chat
import socket

host = '0.0.0.0'  # Escucha en todas las interfaces
port = 8443

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexión entrante desde {client_address}")
print("User2 se ha conectado.")  # Indicar que el otro usuario está conectado

while True:
    message = input("User1: ")  
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    if not data:
        print("User2 se ha desconectado.")  # Indicar que el otro usuario se ha desconectado
        break
    print(f"User2: {data}")  

client_socket.close()
