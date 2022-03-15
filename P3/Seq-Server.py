import socket
import termcolor
import os # Operative System
from Sequence import Seq

PORT = 8080
IP = "127.0.0.1"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket. SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    while True:
        print("Waiting for clients......")
        (client_socket, client_address) = server_socket.accept()

        request_bytes = client_socket.recv(2048)
        request = request_bytes.decode("utf-8")

        slices = request.split(" ")
        command = slices[0]
        termcolor.cprint(f"{command}", 'green')

        response = ""
        if command == "PING":
            response = f"OK!\n"
        elif command == "GET":
            gene_number = int(slices[1])
            gene = GENES[gene_number]
            sequence = Seq()
            #file_name = "../Genes/U5.txt"
            file_name = os.path.join("..", "Genes", f"{gene}.txt")
            sequence.read_fasta(file_name)

            response = f"{sequence}\n"
        elif command == "INFO":
            bases = slices[1]
            sequence = Seq(bases)

            response = f"{sequence.info()}\n"
        elif command == "COMP":
            bases = slices[1]
            sequence = Seq(bases)

            response = f"{sequence.complements()}\n"
        elif command == "REV":
            bases = slices[1]
            sequence = Seq(bases)

            response = f"{sequence.reverse()}\n"
        elif command == "GENE":
            gene = slices[1]
            sequence = Seq()
            file_name = os.path.join("..", "Genes", f"{gene}.txt")
            sequence.read_fasta(file_name)

            response = f"{sequence}\n"
        print(response)
        response_bytes = str.encode(response)
        client_socket.send(response_bytes)

        client_socket.close()
except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")
except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()