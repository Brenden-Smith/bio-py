import modules

def main():
    # Title
    print("""
      ____  _       _____       
     |  _ \(_)     |  __ \      
     | |_) |_  ___ | |__) |   _ 
     |  _ <| |/ _ \|  ___/ | | |
     | |_) | | (_) | |   | |_| |
     |____/|_|\___/|_|    \__, |
                           __/ |
                          |___/ 
                          
        By Brenden Smith""")

    # Menu
    opt=""
    while opt!="0":
        print("""       === === === === ===
        1. Animal Phylum Identifier
        2. DNA/RNA/Amino Acid Transcriber
        === === === === ===
        3. References
        === === === === ===
        0. Exit program
        """)
        opt=input()
        if opt=="1": # Animal Phylum Identifier
            phylum()
        elif opt=="2": # DNA/RNA/Amino Acid Transcriber
            transcriber()
        elif opt=="3": # References
            references()
        elif opt=="0": # Exit program
            print("Now exiting program...")
        else: # Error
            print("Invalid menu input")

def phylum():
    opt=""
    while opt!="0":
        print("""
           ANIMAL PHYLUM 
             IDENTIFIER
        === === === === ===
        1. Add new entry
        2. View previous entries
        3. Clear previous entries
        === === === ==== ===
        0. Return to previous menu
        """)
        opt=input()
        if opt=="1":
            a = modules.Animal()
            a.new()
            modules.orglist.append(a)
            print(f"""
=== === === === ===
Name: {a.name}
Entered Features: {a.features}
Phylum: {a.phylum}
Common Features: {a.commonf}
=== === === === ===""", sep="")
        elif opt=="2":
            if len(modules.orglist) == 0:
                print("There are no previous entries")
            else:
                for i in modules.orglist:
                    print(f"""=== === === === ===
Name: {i.name}
Entered Features: {i.features}
Phylum: {i.phylum}
Common Features: {i.commonf}""", sep="")
                print("=== === === === ===")
        elif opt=="3":
            modules.orglist = []
            print("Entries cleared")
        else:
            print("Invalid input")

def transcriber():
    opt=""
    while opt!="0":
        print("""
            TRANSCRIBER
        === === === === ===
        1. DNA -> RNA
        2. RNA -> DNA
        3. RNA -> Amino Acid
        4. View previous entries
        5. Clear previous entries
        === === === === ===
        0. Return to previous menu
        """)
        opt=input()
        index = len(modules.tlist)
        if len(modules.tlist)==None: index=0
        if opt=="1": # DNA -> RNA
            dtr = modules.DNARNA(index)
            dtr.newentry(1)
            modules.tlist.append(dtr)
        elif opt=="2": # RNA -> DNA
            rtd = modules.DNARNA(index)
            rtd.newentry(2)
            modules.tlist.append(rtd)
        elif opt=="3": # RNA -> Amino Acid
            am = modules.AminoAcid(index)
            am.newaminoacid()
            modules.tlist.append(am)
        elif opt=="4": # View previous entries
            if len(modules.tlist) == 0:
                print("There are no previous entries")
            else:
                for i in modules.tlist:
                    print(f"""=== === === === ===
Index: {i.pos}
Type: {i.mode}
Original ({i.mode2}): {i.original}
New: ({i.mode3}): {i.new}""", sep="")
                print("=== === === === ===")
        elif opt=="5": # Clear previous entries
            modules.tlist = []
            print("Entries cleared")

def references():
    print("""
         References
    === === === === ===
    Animal Phylum Identifier
    https://ib.bioninja.com.au/standard-level/topic-5-evolution-and-biodi/53-classification-of-biodiv/animal-phyla.html
    
    Transcriber
    BIOL 200 Lecture notes
    """)
    dummy=input("Press enter to continue")

if __name__ == '__main__':
    main()