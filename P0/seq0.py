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
    from pathlib import Path

    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    seq = ""
    for line in body:
        seq += line
    return seq

