import http.client
import json
from Sequence import Seq

genes_dict = {"SRCAP": "ENSG00000080603",
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

SERVER = 'rest.ensembl.org'
for gene in genes_dict:
    ENDPOINT = '/sequence/id/' + genes_dict[gene]
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)
    print(f"Gene: {gene} \nDescription: {data1['desc']}")
    sequence = Seq(data1['seq'])
    print(sequence.info())

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()