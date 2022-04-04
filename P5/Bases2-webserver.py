import http.server
import socketserver
import termcolor
from pathlib import Path

IP = "localhost"
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        contents = "I am the happy server! :-)"

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return

    def process_client(s):
        req_raw = s.recv(2000)
        req = req_raw.decode()

        lines = req.split('\n')
        req_line = lines[0]
        slices = req_line.split(" ")
        path = slices[1]
        print("Request line: ", end="")
        termcolor.cprint(req_line, "green")

        body = ""
        if path == "/":
            body = Path("index.html").read_text()
            status_line = "HTTP/1.1 200 OK\n"
        elif path.startswith("/info/"):
            slices = path.split("/")
            resource = slices[2]
            try:
                body = Path(f"{resource}.html").read_text()
                status_line = "HTTP/1.1 200 OK\n"
            except FileNotFoundError:
                body = Path("Error.html").read_text()
                status_line = "HTTP/1.1 404 NOT_FOUND\n"
        else:
            body = Path("Error.html").read_text()
            status_line = "HTTP/1.1 404 NOT_FOUND\n"
        headers = "Content-Type: text/html\n"
        headers += f"Content-Length: {len(body)}\n"
        response_msg = status_line + headers + "\n" + body
        cs.send(response_msg.encode())

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()