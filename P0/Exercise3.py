import seq0

FOLDER = "./sequences/"

list_genes = ["U5", "FRAT1", "ADA", "FXN"]
    for l in list_genes:
        print(l)
        print(len(seq0.seq_read_fasta(FOLDER + l + ".txt")))
