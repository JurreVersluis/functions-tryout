import time
go = "GAME OVER"
gewonnen = "Je hebt gewonnen!"
def animation():
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
def clearconsole():
    for i in range(10):
        print ("")
print("Hallo! Leuk dat je mijn spel: 'IK HEB ZIN IN KOEK!' speelt!", end="")
animation()
clearconsole()
print("je bent opweg naar de koekjes winkel, en je komt bij een kruispunt met 5 verschillende paden", end="")
animation()
keuze1 = input("welke van de 5 paden kies je?\n")
clearconsole()
if keuze1 == "1":
    print("Je loopt verder over het eerste pad" ,end="")
    animation()
    print("En valt van een cliff!\n")
    print(go)
elif keuze1 == "2":
    print("Je loopt verder over het tweede pad, het bos in", end="")
    animation()
    print("Je loopt zo een beer tegen het lijf!", end="")
    animation()
    keuze2 = input("je hebt 2 opties! 1. Je probeert om de beer heen te rennen. Of 2. je probeert hem te vermoorden!\n")
    if keuze2 == "1":
        print("Je rent als Usain Bolt om de beer heen", end="")
        animation()
        print("WHhhooshhhh", end="")
        animation()
        print("Zo naar de koekjeswinkel!")
        print(gewonnen)
    elif keuze2 == "2":
        print("Je probeert de beer te bevechten ", end="")
        animation()
        print("en faalt keihard!")
        print(go)
elif keuze1 == "3":
    print("Je loopt over het derde pad met een zebrapad voorje", end="")
    animation()
    print("Wow er komt een auto aan!", end="")
    animation()
    keuze3 = input("je hebt 2 opties! 1. Je rent snel over het zebrapad voor de auto langs. Of 2. Je wacht rustig tot de auto voorbij is!\n")
    if keuze3 == "1":
        clearconsole()
        print("Je probeert zo snel mogelijk het zebrapad over te rennen", end="")
        animation()
        print("Maar je bent niet optijd en wordt aangereden!")
        print(go)
    elif keuze3 == "2":
        clearconsole()
        print("Je wacht rustig tot de auto voobij is", end="")
        animation()
        clearconsole()
        print("En er komt nog een auto aan", end="")
        animation()
        clearconsole()
        print("En nog twee", end="")
        animation()
        clearconsole()
        print("er ontstaat een file en je je bent niet optijd bij de koekjeswinkel!")
        print(go)
elif keuze1 == "4":
    print("Je loopt rechtstreeks naar de koekjeswinkel", end="")
    animation()
    print("En je ziet een dief alle koekjes stelen", end="")
    animation()
    keuze4 = input("Je hebt twee keuzes: 1. Je rent de koekjesdief achterna 2. Je doet niks en laat hem ontglippen.\n")
    if keuze4 == "1":
        clearconsole()
        print("Je rent de koekjesdief achterna", end="")
        animation()
        print("Je tackelt hem en red de dag!\n")
        print(gewonnen)
    elif keuze4 == "2":
        clearconsole()
        print("Je doet niets aan de koekjesdief", end="")
        animation()
        print("Je loopt naar binnen!", end="")
        animation()
        print("En het blijkt dat de koekjesverkoper gewoon nog een koekje had in zijn kluis!")
        print(gewonnen)
elif keuze1 == "5":
    clearconsole()
    print("je loopt over pad 5 en komt bij nog een kruispunt van 3 paden", end="")
    animation()
    keuze5 = input("Kies je pad 1, 2 of drie?\n")
    if keuze5 == "1":
        clearconsole()
        print("je loopt verder over pad 1", end="")
        animation()
        print("En het blijkt een doodlopend pad te zijn.")
        print(go)
    elif keuze5 == "2":
        clearconsole()
        print("Je loopt verder over pad 2", end="")
        animation()
        print("Het pad loopt zo naar de koekjeswinkel!")
        print("Gewonnen")
    elif keuze5 == "3":
        clearconsole()
        print("je loopt verder over pad 3", end="")
        animation()
        print("je raakt de weg kwijt", end="")
        animation()
        print("maar gelukkig komt je een eekhoorn tegen die je de weg wijst regstreeks naar de koekjeswinkel!\n")
        print(gewonnen)
else:
    print("dat is geen optie, probeer op nieuw!")
#5 losses
#5 wins