"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Zdeněk Pavlásek
email: zpavlasek@gmail.com
"""

import random

pocet_tahu = 0

# ultimatní generovač čisla které neobsahuje duplicitu ani nulu
while True:
    n = str(random.randint(1111, 9999))
    if (n[0] != n[1] and n[0] != n[2] and n[0] != n[3]) and \
       (n[1] != n[2] and n[1] != n[3]) and \
       (n[2] != n[3]) and \
       ('0' not in n):
        break
unikatni_cislo = n
# zakomentovaná nápověda pro testování
print(unikatni_cislo)

# superpodminková silenost která testuje jestli uživatel zadal čislo, jestli jich zadal dostatečný počet nebo 0
while True:
    pocitadlo_bull = 0
    pocitadlo_cows = 0
    n = input("Zajde čtyři čísla: ")
    if n.isdigit():
        if len(n) == 4:
            if (n[0] != n[1] and n[0] != n[2] and n[0] != n[3]) and \
                (n[1] != n[2] and n[1] != n[3]) and \
                (n[2] != n[3]) and ('0' not in n):
                for i in range(len(unikatni_cislo)):
                    if unikatni_cislo[i] == n[i]:
                        pocitadlo_bull += 1
                    elif n[i] in unikatni_cislo:
                        pocitadlo_cows += 1

                if pocitadlo_bull == 4:
                    print("Vyhrál jsi človeče!")
                    print("Počet tahů:", pocet_tahu)
                    break
                else:
                    print("Počet BULL:", pocitadlo_bull)
                    print("Počet COWS:", pocitadlo_cows)
                    pocet_tahu += 1
                    print("Slosování číslo:", pocet_tahu)
                    print("______________________________")
            else:
                print("Obsanuje duplicty nebo 0!!!")
        else:
            print("Špatně zadaná délka čísla!!!!")
    else:
        print("Nezadal jsi cislo!!")
