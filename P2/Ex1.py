from Client0 import Client

print(f"-----| Practice 2, Exercise 1 |------")

IP = "192.168.1.45"
PORT = 8080

c = Client(IP, PORT)

c.ping()

print(f"IP: {c.ip}, {c.port}")