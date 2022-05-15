import http.client
from http import HTTPStatus
import json
from Sequence import Seq

SERVER = "rest.ensembl.org"
PORT = 80

GENES = {"SRCAP": "ENSG00000080603",
         "FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000226906",
         "RBMY2YP": "ENSG00000231436",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

for gene in GENES:
    RESOURCE = f"/sequence/id/{GENES[gene]}?content-type=application/json"
    print()
    print(f"Server: {SERVER}")
    print(f"URL: {SERVER}{RESOURCE}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", RESOURCE)
        r1 = conn.getresponse()
        if r1.status == HTTPStatus.OK:
            print(f"Response received!: {r1.status} {r1.reason}\n")
            print()

            data1 = r1.read().decode("utf-8")
            data1 = json.loads(data1)
            print(f"Gene: {gene} \nDescription: {data1['desc']}")
            sequence = Seq(data1['seq'])
            print(sequence.info())
        else:
            print(f"Invalid response")

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()