def mijnfunctie(antwoord):
    for i in range(11):
        print(antwoord * i)

antwoord = input(f"van welk getal wilt u de tafel zien?")
mijnfunctie(int(antwoord))
