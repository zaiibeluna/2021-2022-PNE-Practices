from Client0 import Client

print(f"-----| Practice 2, Exercise 3 |------")

IP = "192.168.1.45"
PORT = 8080

c = Client(IP, PORT)

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")

