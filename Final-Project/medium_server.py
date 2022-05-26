import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import server as su


PORT = 8080
ENDPOINTS = ["/", "/species", "/karyotype", "/length_chromosome", "/sequence_gene", "/gene_info", "/calculate_gene", "/list_gene"]

socketserver.TCPServer.allow_reuse_address = True

def handle_karyotype(parameters):
    has_error = False
    status = 400
    contents = ""
    if len(parameters) == 1:
        try:
            specie = parameters['specie'][0]
            status, contents = su.karyotype(specie)
        except(KeyError, IndexError):
            has_error = True
    else:
        has_error = True

    return status, contents, has_error

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        url = urlparse(self.path)
        endpoint = url.path
        parameters = parse.query(url.query)
        print("Endpoint:", endpoint)
        print("Parameters:", parameters)

        has_error = False
        contents = ""
        status = 400 # bad request
        if endpoint in ENDPOINTS:
            if endpoint == "/":
                status = 200
                contents = Path("./html/index.html").read_text()
            elif endpoint == "/species":
                if len(parameters) == 0:
                    status, contents = su.species()
                elif len(parameters) == 1:
                    try:
                        limit = int(parameters['limit'][0])
                        status, contents = su.species(limit)
                    except(KeyError, ValueError, IndexError):
                        has_error = True
                else:
                    has_error = True
            elif endpoint == "/karyotype":
                status, contents, has_error = handle_karyotype(parameters)

            elif endpoint == "/length_chromosome":
                if len(parameters) == 2:
                    try:
                        specie = parameters['specie'][0]
                        chromo = int(parameters['chromo'][0])
                        status, contents = su.length_chromosome(specie, chromo)
                    except(KeyError, IndexError):
                        has_error = True
                else:
                    has_error = True

            elif endpoint == "/sequence_gene":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.sequence_gene(gene)
                    except(KeyError, IndexError):
                        has_error = True
                else:
                    has_error = True

            elif endpoint == "/gene_info":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.gene_info(gene)
                    except(KeyError, IndexError):
                        has_error = True
                else:
                    has_error = True

            elif  endpoint == "/calculate_gene":
                if len(parameters) == 1:
                    try:
                        gene = parameters['gene'][0]
                        status, contents = su.calculate_gene(gene)
                    except(KeyError, IndexError):
                        has_error = True
                else:
                    has_error = True

            elif endpoint == "/list_gene":
                if len(parameters) == 3:
                    try:
                        chromo = parameters['chromo'][0]
                        start = int(parameters['start'][0])
                        end = int(parameters['end'][0])
                        status, contents = su.list_gene(chromo, start, end)
                    except(KeyError, ValueError, IndexError):
                        has_error = True
                else:
                    has_error = True

        else:
            has_error = True

        if has_error:
            contents = Path("./html/error.html").read_text()

        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())

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