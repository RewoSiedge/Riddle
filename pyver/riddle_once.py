import itertools
def idk_man(ausgangswort):
    anagramme = set(["".join(perm) for perm in itertools.permutations(ausgangswort)])
    return anagramme

anagramme = []
def permuddation(wort, erstes, laenge):
    if erstes == laenge - 1:
        anagramme.append(wort)
        return
    zweites = erstes
    while zweites < laenge:
        schliste = list(wort)
        schliste[erstes], schliste[zweites] = schliste[zweites], schliste[erstes]
        wort = "".join(schliste)
        permuddation(wort, erstes + 1, laenge)
        schliste[zweites], schliste[erstes] = schliste[erstes], schliste[zweites]
        wort = "".join(schliste)
        zweites += 1

def findus(starr, strong):
    niedergang = 0
    uebergang = len(starr) - 1
    while niedergang <= uebergang:
        mitte = int((niedergang + uebergang) / 2)
        if starr[mitte] == strong:
            return mitte
        elif strong < starr[mitte]:
            uebergang = mitte - 1
        elif strong > starr[mitte]:
            niedergang = mitte + 1
    return -1

woerter = open("german.dic", "r", encoding = "latin-1")
woerterliste = woerter.readlines()
woerterliste = [i.lower().strip("\n") for i in woerterliste]
woerter.close()
wort = "blumentopf"
permuddation(wort, 0, len(wort))
j = False 

for i in anagramme:
    if findus(woerterliste, i) != -1 and i != wort:
        print(i, "\n")
        j = True
if j == False:
    print("\ndazu gibt es leider nichts :(\n")
