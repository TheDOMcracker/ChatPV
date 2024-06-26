# Cliente de chat
import socket

host = 'dirección_ip_del_servidor'  # Reemplaza con la dirección IP del servidor
port = 8443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Conectado a User1.")  # Indicar que el otro usuario está conectado

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        print("User1 se ha desconectado.")  # Indicar que el otro usuario se ha desconectado
        break
    print(f"User1: {data}")  
    message = input("Tú: ")  
    client_socket.send(message.encode())

client_socket.close()
