import http.client
import json

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

list_values = genes_dict.values()

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)

    print("Dictionary of Genes!")
    print(f"There are {len(list_values)} genes in the dictionary:")
    for k,v in genes_dict.items():
        print(f"{k}--->{v}")
    
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()