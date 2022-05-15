import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import commands

PORT = 8080

HTML_folder = "./html_files/"

def read_file(filename):
    contents = Path(HTML_folder + filename).read_text()
    contents = j.Template(contents)
    return contents

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        query = url_path.query

        command_dict = parse_qs(query)

        t.cprint(path, "yellow")
        t.cprint(query, "green")
        t.cprint(command_dict, "blue")

        if path == "/":
            contents = Path("./html/index.html").read_text()
        elif path == "/favicon.ico":
            contents = Path("./html/index.html").read_text()
        elif path == "/list":
            ENDPOINT = "/info/species"
            PARAMS = "?content-type=application/json"

            species_dict = commands.make_request(ENDPOINT, PARAMS)
            species = ""
            limit = int(command_dict["limit"][0])

            if limit > len(species_dict["species"]) or 0 > limit:
                contents = read_file("error.html").render(context={"error": "Please enter a validlimit value, between o and" + str(len(species_dict["species"]))})
            else:
                for b in range(o, int(limit)):
                    species = species + "<br>&nbsp&nbsp&nbsp&nbsp· " + species_dict["species"][b]["name"]

                contents = read_file(path[1:] + ".html").render(context={"length": str(len(species_dict["species"])), "limit": limit, "species": species})

        elif path == "/karyotype":
            ENDPOINT = "/info/assembly/" + command_dict["species"][0].strip()
            PARAMS = "?content-type=application/json"

            karyotype_dict = commands.make_request(ENDPOINT, PARAMS)

            try:
                chromosomes = ""
                for e in karyotype_dict["karyotype"]:
                    chromosomes = chromosomes + "<br>&nbsp&nbsp&nbsp&nbsp· " + e
                if chromosomes.replace("<br>&nbsp&nbsp&nbsp&nbsp· ", "") == "":
                    contents = read_file(path[1:] + ".html").render(context={"karyotype": chromosomes})

                else:
                    contents = read_file(path[1:] + ".html").render(context={"karyotype": chromosomes})

            except KeyError:
                contents = read_file("error.html").render(context={"error": "karyotype for " + command_dict["species"][0] + " not found"})

        elif path == "/chromosome":
            ENDPOINT = "/info/assembly/" + command_dict["species"][0].strip()
            PARAMS = "?content-type=application/json"

            species_dict = commands.make_request(ENDPOINT, PARAMS)

            try:
                chromosome_dict = species_dict["top_level_region"]
                correct = False
                i = 0

                while not correct and i < len(chromosome_dict):
                    chromosome = chromosome_dict[i]
                    if chromosome["name"] == command_dict["chormosome"]:
                        correct = True
                    print(correct)
                    i += 1
                chromosome_length = chromosome["length"]
                contents = read_file(path[1:] + ".html").render(context={"Chromosome": chromosome["name"], "chromosome_length": chromosome_length})
            except IndexError:
                contents = read_file("error.html").render(context={"error": "Chromosome for " + command_dict["chromosome"][0] + " not found"})
            except KeyError:
                contents = read_file("error.html").render(context={"error": "karyotype for " + command_dict["species"][0] + " not found"})

        elif path =="/sequence_gene":
            try:
                ENDPOINT = "/sequence/id/"
                PARAMS = "?content-type=application/json"

                gene_dict = commands.make_request(ENDPOINT + command_dict["id"][0], PARAMS)
                seq = Seq(gene_dict["seq"])
                if seq.valid_sequence():
                    contents = read_file(sequence_gene.html).render(context={"seq": str(seq), "gene": command_dict["id"][0]})
                else:
                    contents = "Incorrect sequence, please enter a correct one."
            except KeyError:
                contents = read_file("error.html").render(context={"error": "Gene with id " + command_dict["id"][0] + " not found"})

        elif path =="/calculate_gene":
            try:
                ENDPOINT = "/sequence/id/"
                PARAMS = "?content-type=application/json"

                gene_dict = commands.make_request(ENDPOINT + command_dict["id"][0], PARAMS)
                seq = Seq(gene_dict["seq"])
                if not seq.valid_sequence():
                    contents = read_file("error.html").render(context={"error": "Incorrect sequence, please enter a correct one."})
                else:
                    n_bases = seq.bases()
                    percentages = seq.base_percentage()
                    seq_len = seq.len()
                    contents = "\nTotal length: " + str(seq_len) + "\n"
                    for p in percentages:
                        contents = contents + str(p) + ": " + str(n_bases[p]) + " (" + str(percentages[p]) + "%)\n"
                    contents = contents.replace("\n", "<p><p>")
                    contents = read_file(path[1:] + ".html").render(context={"result": contents, "seq": seq})
            except KeyError:
                contents = read_file("error.html").render(context={"error": "Gene with id " + command_dict["id"][0] + " not found"})

        self.send_response(200)
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