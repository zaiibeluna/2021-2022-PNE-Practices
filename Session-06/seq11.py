class Seq:
    """A class for representing sequences"""

    BASES_ALLOWED = ['A', 'C', 'G', 'T']

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

    def __init__(self, bases):
        if Seq.are_bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.bases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.bases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, bases, name=""):

        super().__init__(bases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.bases

print(Seq.are_bases_valid("ACXT"))

