import itertools
def idk_man(ausgangswort):
    anagramme = set(["".join(perm) for perm in itertools.permutations(ausgangswort)])
    return anagramme
woerter = open("/Users/alice/Downloads/german/german.dic", "r", encoding = "latin-1")
woerterliste = woerter.readlines()
woerterliste = [i.lower().strip("\n") for i in woerterliste]
woerter.close()
while True:
    wort = input("try me ")
    j = False
    for i in idk_man(wort):
        if i in woerterliste and i != wort:
            print(i, "\n")
            j = True
            continue
    if j == False:
        print("\ndazu gibt es leider nichts\n")