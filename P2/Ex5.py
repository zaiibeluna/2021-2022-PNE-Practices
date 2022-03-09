from Client0 import Client
from Seq1 import Seq

GENE = "FRAT1"
FRAGMENTS = 5
BASES = 10

print(f"-----| Practice 2, Exercise 5 |------")

IP = "192.168.1.45"
PORT = 8080

c = Client(IP, PORT)

s = Seq()
s.read_fasta(f"../Genes/{gene}.txt")

print(f"Gene {GENE}: {s}")

c.debug_talk(f"Sending {gene} Gene to the server, in fragments of {BASES} bases")

start_index = 0
end_index = BASES
for f in range(1, FRAGMENTS + 1):
    fragment = s.bases[0: BASES]
    print(f"Fragment {f}: {fragment}")
    c-debug_talk(fragment)
    start_index += BASES
    end_index += BASES

