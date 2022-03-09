from Client0 import Client

print(f"-----| Practice 2, Exercise 4 |------")

IP = "192.168.1.45"
PORT = 8080

c = Client(IP, PORT)

gene_list = ["U5", "FRAT1", "ADA"]
for gene in gene_list:
    s = Seq()
    s.read_fasta(f"../Genes/{gene}.txt")
    c.debug_talk(f"Sending {gene} Gene to the server...")
    c.debug_talk(str(s))
    print(c)