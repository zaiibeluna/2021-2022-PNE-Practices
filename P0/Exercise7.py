from seq0 import *

FOLDER = "../Session-04/"
GENES = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

print("----|Exercise 7|----")

for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}:")
    frag = sequence[:20]
    print(f"Frag: {frag}")
    print(f"Comp: {seq_complement(frag)}")
    print()

