class Animal():
    def __init__(self):
        self.name = None
        self.phylum = None
        self.features = []
        self.commonf = []

    def new(self):
        self.name = input("Enter animal's entry name: ")
        print()
        print("You will now begin a questionnaire to determine the phylum of your animal")

        # Determination tree
        ver = self.backbone()
        if ver==1: # Vertebrate
            self.chordata()
            return
        elif ver==2: # Invertebrate
            sym = self.symmetry()
            if sym==1: # Asymmetrical
                self.porifera()
                return
            elif sym==2: # Radial
                self.cnidaria()
                return
            elif sym==3: # Bilateral
                bc = self.bodycavity()
                if bc==1: # Mouth but no anus
                    self.platyhelmintha()
                    return
                elif bc==2: # Mouth but no anus
                    seg = self.segmentation()
                    if seg==1: # Segmented
                        oth = self.other()
                        if oth==1: # Peristalsis
                            self.annelida()
                            pass
                        elif oth==2: # Exoskeleton
                            self.arthropoda()
                            pass
                    elif seg==2: # Non-visible
                        self.mollusca()
                        return

    def backbone(self):
        opt = ""
        while opt != "1" and opt != "2":
            print("""
                         BACKBONE
                    === === === === ===
                    1. Vertebrate
                    2. Invertebrate
            """)
            opt = input()
            if opt == "1":
                self.features.append("Vertebrate")
                return 1
            elif opt == "2":
                self.features.append("Invertebrate")
                return 2
            else:
                print("Invalid input")

    def symmetry(self):
        opt = ""
        while opt != "1" and opt != "2" and opt != "3":
            print("""
                         SYMMETRY
                    === === === === ===
                    1. Asymmetrical
                    2. Radial
                    3. Bilateral
            """)
            opt = input()
            if opt=="1":
                self.features.append("Asymmetrical")
                return 1
            elif opt=="2":
                self.features.append("Radial")
                return 2
            elif opt=="3":
                self.features.append("Bilateral")
                return 3
            else:
                print("Invalid input")

    def bodycavity(self):
        opt = ""
        while opt != "1" and opt != "2":
            print("""
                        BODY CAVITY
                    === === === === ===
                    1. Mouth but no anus
                    2. Mouth and anus
            """)
            opt = input()
            if opt == "1":
                self.features.append("Mouth but no anus")
                return 1
            elif opt == "2":
                self.features.append("Mouth and anus")
                return 2
            else:
                print("Invalid input")

    def segmentation(self):
        opt = ""
        while opt != "1" and opt != "2":
            print("""
                        SEGMENTATION
                    === === === === ===
                    1. Segmented
                    2. Non-visible (mantle & foot)
                    """)
            opt = input()
            if opt == "1":
                self.features.append("Segmented")
                return 1
            elif opt == "2":
                self.features.append("Non-visible (mantle & foot)")
                return 2
            else:
                print("Invalid input")

    def other(self):
        opt = ""
        while opt != "1" and opt != "2":
            print("""
                           OTHER
                    === === === === ===
                    1. Move via peristalsis
                    2. Exoskeleton (chitin)
                    """)
            opt = input()
            if opt == "1":
                self.features.append("Move via peristalsis")
                return 1
            elif opt == "2":
                self.features.append("Exoskeleton (chitin)")
                return 2
            else:
                print("Invalid input")

    def porifera(self):
        self.phylum = "Porifera"
        self.commonf.append("Invertebrate")
        self.commonf.append("Asymmetrical")
        self.commonf.append("Pores for body cavities")
        self.commonf.append("No segmentation")
        self.commonf.append("Spicules for support")

    def cnidaria(self):
        self.phylum = "Cnidaria"
        self.commonf.append("Invertebrate")
        self.commonf.append("Radial symmetry")
        self.commonf.append("Mouth but no anus")
        self.commonf.append("No segmentation")
        self.commonf.append("Stinging cells (cnidocytes)")

    def platyhelmintha(self):
        self.phylum = "Platyhelmintha"
        self.commonf.append("Invertebrate")
        self.commonf.append("Bilateral symmetry")
        self.commonf.append("Mouth but no anus")
        self.commonf.append("No segmentation")
        self.commonf.append("Flattened body")

    def annelida(self):
        self.phylum = "Annelida"
        self.commonf.append("Invertebrate")
        self.commonf.append("Bilateral symmetry")
        self.commonf.append("Mouth and anus")
        self.commonf.append("Segmented")
        self.commonf.append("Move via peristalsis")

    def mollusca(self):
        self.phylum = "Mollusca"
        self.commonf.append("Invertebrate")
        self.commonf.append("Bilateral symmetry")
        self.commonf.append("Mouth and anus")
        self.commonf.append("Non-visible (mantle & foot) segmentation")
        self.commonf.append("May have a shell (made by mantle")

    def arthropoda(self):
        self.phylum = "Arthropoda"
        self.commonf.append("Invertebrate")
        self.commonf.append("Bilateral symmetry")
        self.commonf.append("Mouth and anus")
        self.commonf.append("Segmented")
        self.commonf.append("Exoskeleton (chitin)")

    def chordata(self):
        self.phylum = "Chordata"
        self.commonf.append("Vertebrate")
        self.commonf.append("Bilateral symmetry")
        self.commonf.append("Pores for body cavities")
        self.commonf.append("No segmentation")
        self.commonf.append("Spicules for support")

class DNARNA():
    def __init__(self, i : int):
        self.pos = i
        self.dna = None
        self.rna = None
        self.original = None
        self.new = None
        self.mode = None
        self.mode2 = None
        self.mode3 = None

    def newentry(self, mode : int):
        if mode==1: # DNA -> RNA
            self.dna=input("Enter DNA String: ")
            self.original = self.dna
            self.rna = self.dnatorna()
            self.new = self.rna
            self.mode = "DNA -> RNA"
            self.mode2 = "DNA"
            self.mode3 = "RNA"
        else: # RNA -> DNA
            self.rna = input("Enter RNA String: ")
            self.original = self.rna
            self.dna = self.rnatodna()
            self.new = self.dna
            self.mode = "RNA -> DNA"
            self.mode2 = "RNA"
            self.mode3 = "DNA"
        print(f"""=== === === === ===
Index: {self.pos}
Type: {self.mode}
Original ({self.mode2}): {self.original}
New: ({self.mode3}): {self.new}
=== === === === ===""", sep="")

    def dnatorna(self):
        # Test String: ACGTTACGGATTACAGTCCCAAACTAC
        # Expected Output: UGCAAUGCCUAAUGUCAGGGUUUGAUG
        new = ""
        for element in self.dna:
            if element == "A": new = new+"U"
            elif element == "C": new = new+"G"
            elif element == "T": new = new+"A"
            elif element == "G": new = new+"C"
            else: new = new+"?"
        return str(new)

    def rnatodna(self):
        # Test String: UGCAAUGCCUAAUGUCAGGGUUUGAUG
        # Expected Output: ACGTTACGGATTACAGTCCCAAACTAC
        new = ""
        for element in self.rna:
            if element == "U": new = new + "A"
            elif element == "G": new = new + "C"
            elif element == "A": new = new + "T"
            elif element == "C": new = new + "G"
            else: new = new + "?"
        return str(new)

class AminoAcid:
    def __init__(self, i : int):
        self.pos = i
        self.original = None
        self.new = None
        self.mode = "RNA -> Amino Acid"
        self.mode2 = "RNA"
        self.mode3 = "Amino Acid"

    def newaminoacid(self):
        self.original = input("Enter RNA String: ")
        self.new = self.rnatoamino()
        print(f"""=== === === === ===
Index: {self.pos}
Type: {self.mode}
Original ({self.mode2}): {self.original}
New: ({self.mode3}): {self.new}
=== === === === ===""", sep="")

    def rnatoamino(self):
        # Test String: UAAUGUGUCGAAUCUAAGC
        # Expected Output: Met Cys Arg Ile Stop
        new=""
        start=False
        k=0
        for i in range(len(self.original)):
            if i <= 3:
                pass
            elif k % 3 == 0 and start==True:
                third = self.original[i]
                second = self.original[i+1]
                first = self.original[i+2]
                set = str(third + second + first)
                if set == "UAA" or set == "UAG" or set == "UGA":
                    new += "Stop "
                    return str(new)
                if set == "UUU" or set == "UUC":
                    new += "Phe "
                elif set == "UUA" or set == "UUG":
                    new += "Leu "
                elif set == "UCU" or set == "UCC" or set == "UCA" or set == "UCG":
                    new += "Ser "
                elif set == "UAU" or set == "UAC":
                    new += "Tyr "
                elif set == "UGU" or set == "UGC":
                    new += "Cys "
                elif set == "UGG":
                    new += "Trp "
                elif set == "CUU" or set == "CUC" or set == "CUA" or set == "CUG":
                    new += "Leu "
                elif set == "CCU" or set == "CCC" or set == "CCA" or set == "CCG":
                    new += "Pro "
                elif set == "CAU" or set == "CAC":
                    new += "His "
                elif set == "CAA" or set == "CAG":
                    new += "Gln "
                elif set == "CGU" or set == "CGC" or set == "CGA" or set == "CGG":
                    new += "Arg "
                elif set == "AUU" or set == "AUC" or set == "AUA":
                    new += "Ile "
                elif set == "AUG":
                    new += "Met "
                elif set == "ACU" or set == "ACC" or set == "ACA" or set == "ACG":
                    new += "Thr "
                elif set == "AAU" or set == "AAC":
                    new += "Asn "
                elif set == "AAA" or set == "AAG":
                    new += "Lys "
                elif set == "AGU" or set == "AGC":
                    new += "Ser "
                elif set == "AGA" or set == "AGG":
                    new += "Arg "
                elif set == "GUU" or set == "GUC" or set == "GUA" or set == "GUG":
                    new += "Val "
                elif set == "GCU" or set == "GCC" or set == "GCA" or set == "GCG":
                    new += "Ala "
                elif set == "GAU" or set == "GAC":
                    new += "Asp "
                elif set == "GAA" or set == "GAG":
                    new += "Glu "
                elif set == "GGU" or set == "GGC" or set == "GGA" or set == "GGG":
                    new += "Gly "
                k+=1
            elif start==False:
                third=self.original[i-2]
                second=self.original[i-1]
                first=self.original[i]
                set=str(third+second+first)
                if set == "AUG":
                    start = True
                    new += "Met "
                    k=3
            elif start==True:
                k+=1
        return Exception("Could not find end segment UAA")



orglist = []
tlist = []