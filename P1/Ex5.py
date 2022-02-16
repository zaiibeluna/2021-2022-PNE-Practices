from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("ATTXXG")

print("Sequence 1: ", s1)
print("Sequence 2: ", s2)
print("Sequence 3: ", s3)

if Seq.valid_sequence(s1):
    print("Sequence 1:","Length: ",str(s1.len()),str(s1))
else:
    print("ERROR")

if Seq.valid_sequence(s2):
    print("Sequence 2:","Length: ",str(s2.len()),str(s2))
else:
    print("ERROR")

if Seq.valid_sequence(s3):
    print("Sequence 3:","Length: ",str(s3.len()),str(s3))
else:
    print("ERROR")

