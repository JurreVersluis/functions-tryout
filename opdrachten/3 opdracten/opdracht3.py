

def zeg(jaar, naam):
    naam = input("wat is je naam?\n")
    if naam == "stop":
        exit()
    jaar = input("wat is je leeftijd?\n")
    if jaar == "stop":
        exit()
    print(f"U bent {jaar} jaar oud en uw naam is: {naam}")
    zeg(jaar, naam)

zeg("", "")

