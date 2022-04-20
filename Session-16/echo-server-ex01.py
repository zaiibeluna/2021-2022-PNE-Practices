import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        if self.path =="/":
            contents = Path('form-1.html').read_text()
            self.send_response(200)
        elif self.path.startswith("/echo?"):
            parsed_url = urlparse(self.path)
            params = parse_qs(parsed_url.query)
            try:
                msg_param = params['msg'][0]
                contents = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Result</title>
                        </head>
                        <body>
                            <h1>Received message:</h1>
                            <p>{msg_param}</p>
                            <a href="/">Main page</a>
                        </body>
                    </html>"""
                self.send_response(200)
            except (KeyError, IndexError):
                contents = Path(f"Error.html").read_text()
                self.send_response(404)
        else:
            contents = Path(f"Error.html").read_text()
            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()