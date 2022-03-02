from Seq1 import Seq

print("--- Exercise 1 ---")
my_seq = Seq("ACTGA")

if Seq.valid_sequence(my_seq):
    print("Sequence 1:","Length: ",str(my_seq.len()), str(my_seq))
else:
    print("ERROR")

