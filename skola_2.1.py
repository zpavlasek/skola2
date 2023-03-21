"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zdeněk Pavlásek
email: zpavlasek@gmail.com
"""

# upravl jsem generator kodu
# upravil jsem rozlišení Bulls a Bull a COWS a COW
# pridal jsem oznameni pokud uzivatel vyhraje na prvni pokus.
# taky jsem pridal ze se muze pracovat s nulou.


import random
# priznam se ze jsem generator uplně sam nevymyslel ale poctivě jsem ukradl jeho časti na google a upravil ho :)
unikatni_cislo = str(random.sample(range(1000, 10000), 1)[0])
while unikatni_cislo[0] == '0' or len(set(unikatni_cislo)) < 4:
    unikatni_cislo = str(random.sample(range(1000, 10000), 1)[0])

pocet_tahu = 1

# napoveda
print(unikatni_cislo)

while True:
    pocitadlo_bull = 0
    pocitadlo_cows = 0
    n = input("Zadej čtyřmístné číslo: ")
    if n.isdigit():
        if len(n) == 4:
            if (n[0] != n[1] and n[0] != n[2] and n[0] != n[3]) and \
                (n[1] != n[2] and n[1] != n[3]) and \
                (n[2] != n[3]) and (n[0] != '0'):
                for i in range(len(unikatni_cislo)):
                    if unikatni_cislo[i] == n[i]:
                        pocitadlo_bull += 1
                    elif n[i] in unikatni_cislo:
                        pocitadlo_cows += 1

                if pocitadlo_bull == 4:
                    print("Vyhrál jsi člověče!")
                    if pocet_tahu == 1:
                        print("Uhodl jsi to na 1. pokus!")
                    else:
                        print("Uhodl jsi to na", pocet_tahu, "pokusů.")
                    break
                else:
                    if pocitadlo_bull == 1:
                        bull_text = "BULL"
                    else:
                        bull_text = "BULLS"
                    if pocitadlo_cows == 1:
                        cow_text = "COW"
                    else:
                        cow_text = "COWS"
                    print("Počet", bull_text + ":", pocitadlo_bull)
                    print("Počet", cow_text + ":", pocitadlo_cows)
                    pocet_tahu += 1
                    print("Slosování číslo:", pocet_tahu)
                    print("______________________________")
            else:
                print("Zadané číslo obsahuje duplicity nebo začíná nulou!")
        else:
            print("Zadané číslo nemá délku 4!")
    else:
        print("Zadaná hodnota není číslo!")
