import http.server
import socketserver
import termcolor
from pathlib import Path
import os
from Sequence import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

GENES = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        contents = Path('form-1.html').read_text()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')
    req_line = lines[0]
    slices = req_line.split(" ")
    path = slices[1]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    body = ""
        if path == "PING":
            body = Path("form-1.html").read_text()
        elif path == "GET":
            gene_number = int(slices[1])
            gene = GENES[gene_number]
            sequence = Seq()
            file_name = os.path.join("..", "Genes", f"{gene}.txt")
            sequence.read_fasta(file_name)
            body = Path("form-2.html").read_text()
        elif path == "GENE":
            gene = slices[1]
            sequence = Seq()
            file_name = os.path.join("..", "Genes", f"{gene}.txt")
            sequence.read_fasta(file_name)
            body = Path("form-3.html").read_text()
        elif path == "Operation":
            if option == "info":
                bases = slices[1]
                sequence = Seq(bases)
            elif option == "complement":
                bases = slices[1]
                sequence = Seq(bases)
            elif option == "reverse":
                bases = slices[1]
                sequence = Seq(bases)
            body = Path("form-3.html").read_text()
        status_line = "HTTP/1.1 200 OK\n"
        headers = "Content-Type: text/html\n"
        headers += f"Content-Length: {len(body)}\n"
        response_msg = status_line + headers + "\n" + body
        cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured!")

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()