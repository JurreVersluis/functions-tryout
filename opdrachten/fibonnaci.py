getal1 = 0
getal2 = 1
count = 0
hoeveelKeer = int(input("hoeveel getallen van fibbonaci wil je?"))

for i in range(hoeveelKeer):
    x = lambda a, b,: a + b
    count = (x(getal1, getal2))
    getal1 = getal2
    getal2 = count
    count += 1
    print(getal1)

