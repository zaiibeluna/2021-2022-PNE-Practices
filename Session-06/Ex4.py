import termcolor
from seq11 import Seq

def generate_seqs(pattern, number):
    result = []
    for n in range(1, number + 1):
        result.append(Seq(pattern * n))
    return result

def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        termcolor.cprint(f"Sequence {index}: (Length: {seq.len()}) {seq}", color)

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')