import socket

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.listen()

print("The server is configured!")

print("Waiting for Clients to connect")
(client_socket, client_address) = ls.accept()

print("A client has connected to the server!")

msg_bytes = cs.recv(2048)
msg = msg_bytes.decode("utf-8")
print(f"Received Message: {msg}")
response = "HELLO. I am the Happy Server :-)\n"
response_bytes = response.encode()
cs.send(response_bytes)

cs.close()
ls.close()