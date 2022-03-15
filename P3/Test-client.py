from Seq-Client import Client

PORT = 8080
IP = "127.0.0.1"
BASES = ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

c = client(PORT, IP)
print(c)

c.debug_talk("PING")

print()

for n in range(5):
    c.debug_talk(f"GET {n}")
    print()

c.debug_talk(f"INFO {BASES}")

print()

c.debug_talk(f"COMP {BASES}")

print()

c.debug_talk(f"REV {BASES}")

print()

for gene in GENES:
    c.debug_talk(f"GENE {gene}")
    print()