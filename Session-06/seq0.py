BASES = ["A", "T", "C", "G"]
COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

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

def seq_len(seq):
    return len(seq)

def seq_count_base(seq: str, base):
    return seq.count(base)

def seq_count(seq):
    result = {}
    for base in BASES:
        result[base] = seq_count_base(seq, base)
    return result

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    result = ""
    for base in seq:
        result += COMPLEMENTS[base]
    return result

def most_frequent_base(seq):
    max_base = None
    max_count = 0
    for base, count in seq_count(seq).items():
        if count >= max_count:
            max_base = base
            max_count = count
    return max_base


