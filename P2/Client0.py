class Client:

    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def ping(self):
        print("OK")

    def __str__(self):
        result = (f"Connection to SERVER at {self.ip} PORT: {self.port}")
        return result

    def talk(self, msg):
        import socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))

        msg_bytes = str.encode(msg)
        client_socket.send(msg_bytes)

        response_bytes = client_socket.recv(2048)
        response = response_bytes.decode("utf-8")

        client_socket.close()

        return response



