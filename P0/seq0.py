def seq_ping():
    print("OK")

def valid_filename():
    exit = False
    while not exit:
        FOLDER = "./sequences/"
        filename = input("What file do you want to open?")
        try:
            f = open(FOLDER + filename + ".txt")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file.")

def seq_read_fasta(filename):
    FOLDER = "./sequences/"
    seq = open(FOLDER + filename + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

