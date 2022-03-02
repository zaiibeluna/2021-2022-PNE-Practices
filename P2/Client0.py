class Client:

    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def ping(self):
        print("OK")

    def __str__(self):
        result = (f"Connection to SERVER at {self.ip} PORT: {self.port}")
        return result

    def talk(self):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response



