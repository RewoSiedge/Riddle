import itertools
def idk_man(ausgangswort):
    anagramme = set(["".join(perm) for perm in itertools.permutations(ausgangswort)])
    return anagramme

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
j = False
starr = idk_man(wort)

for i in starr:
    if findus(woerterliste, i) != -1 and i != wort:
        print(i, "\n")
        j = True
if j == False:
    print("\ndazu gibt es leider nichts :(\n")
