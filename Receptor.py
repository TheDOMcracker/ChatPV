# Cliente de chat
import socket

host = 'dirección_ip_del_servidor'  # Reemplaza con la dirección IP del servidor
port = 8443  # Cambia el puerto al 8443 o el puerto que hayas seleccionado

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    data = client_socket.recv(1024).decode()
    print(f"Johangel: {data}")  # Cambia "Johangel" a [tu nombre]

    message = input("Yulianny: ")  # Cambia "Yulianny" a [la persona que recibe]
    client_socket.send(message.encode())

client_socket.close()
