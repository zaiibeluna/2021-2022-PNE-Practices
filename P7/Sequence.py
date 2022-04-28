class Seq:
    """A class for representing sequences"""

    BASES_ALLOWED = ['A', 'C', 'G', 'T']
    COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, bases="NULL" ):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.bases = bases
        if self.bases == "NULL":
            self.bases = bases
            print("NULL Seq created!")
        elif self.are_bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INVALID sequence detected!")

    @staticmethod
    def are_bases_valid(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] in Seq.BASES_ALLOWED:
                i += 1
            else:
                valid = False
        return valid

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.bases

    def len(self):
        """Calculate the length of the sequence"""
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        result = {}
        for base in Seq.BASES_ALLOWED:
            result[base] = self.count_base(base)
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        return self.bases[::-1]

    def complements(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        for base in self.bases:
            result += Seq.COMPLEMENTS[base]
        return result

    def read_fasta(self, file_name):
        from pathlib import Path

        file_contents = Path(file_name).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = "" #importante ponerlo
        for line in body:
            self.bases += line

    def info(self):
        result = f"Sequence: {self.bases}\n"
        result += f"Total length: {self.len()}\n"
        for base, count in self.count().items():
            result += f"{base}: {count} ({(count * 100) / self.len():.1f}%)\n"
        return result

    def add(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            print("We could not multiply the bases since the sequence is not correct.")
        else:
            result = {}
            for base in Seq.BASES_ALLOWED:
                result[base] = self.count_base(base)
                add = result[base] + result[base]
            return add

