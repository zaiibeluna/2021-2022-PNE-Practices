from Seq1 import Seq

print("-----| Exercise 6 |------")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Length: {seq.len()}) {seq}")
    print(f"\tBases: {seq.count()}")