from seq0 import *

FOLDER = "../Session-04/"
GENES = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]

print("----|Exercise 6|----")

for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}:")
    frag = sequence[:20]
    print(f"Frag: {frag}")
    print(f"Rev: {seq_reverse(frag)}")
    print()
