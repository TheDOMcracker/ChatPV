# Servidor de chat
import socket

host = '0.0.0.0'  # Escucha en todas las interfaces
port = 8443  # Cambia el puerto al 8443 o cualquier otro puerto seguro que prefieras

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexión entrante desde {client_address}")

while True:
    message = input("Johangel: ")  # Cambia "Tú" a "Johangel"
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"Yulianny: {data}")  # Cambia "Yulianny" a la persona receptora

client_socket.close()
