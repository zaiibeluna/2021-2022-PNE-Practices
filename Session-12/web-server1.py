import socket
import termcolor


IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # HTTP Request
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')
    req_line = lines[0] # "GET /directory/other/file.html HTTP/1.0"
    slices = req_line.split(" ")
    method = slices[0] # "GET"
    path = slices[1] # "/directory/other/file.html"
    version = slices[2] # "HTTP/1.0"
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # HTTP Response
    body = "Hello from my first web server!\n"
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/plain\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)

        cs.close()