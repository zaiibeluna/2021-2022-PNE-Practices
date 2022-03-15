import socket
import termcolor


PORT = 8000
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

number_con = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((IP, PORT))
    server_socket.listen(MAX_OPEN_REQUESTS)
    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = server_socket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        msg = client_socket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        message = "Hello from the teacher's server"
        send_bytes = str(message).encode()
        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()