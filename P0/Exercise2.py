import seq0

FOLDER = "../Session-04/"

filename = input("File's name: ")
print(f"DNA file: {filename}")
seq = sequence = seq0.seq_read_fasta(FOLDER + filename)
print("The first 20 bases are: ", sequence[:20])
print(sequence)
