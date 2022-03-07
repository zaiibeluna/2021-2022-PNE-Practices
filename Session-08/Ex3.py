import socket

# Teacher's server
PORT = 8000
IP = "localhost"

while True:
    msg = input("Introduce your message in the chat: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    msg_bytes = str.encode(msg)
    client_socket.send(msg_bytes)

    client_socket.close()