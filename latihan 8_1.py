def membandingkan_file(fileA, fileB):
    with open(fileA, 'r') as fA, open(fileB, 'r') as fB:
        while True:
            line1 = fA.readline()
            line2 = fB.readline()
            if not line1 and not line2:
                break
            if line1!= line2:
                print(f"Difference at line {fA.tell()}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")

membandingkan_file('pA.txt', 'pB.txt')
