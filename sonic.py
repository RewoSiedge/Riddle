# sonic the hedgehog yk :)
# Geschwindigkeit messen von c++ und python

import string
import sys
import subprocess
from subprocess import DEVNULL
import resource
import matplotlib.pyplot as plt
import csv

# Liste von Konsonanten
konsonanten = [letter for letter in list(string.ascii_lowercase) if letter not in ["a", "e", "i", "o", "u"]]

if __name__ == "__main__":
    try:
        von = int(sys.argv[1])
        bis = int(sys.argv[2])
    except ValueError:
        print("bist scheiße. format: sonic.py [kleinste wortlänge] [größte]")
        sys.exit(1)
    except IndexError:
        von = 1
        bis = 12

    zeitencpp = []
    zeitenpy = []
    for i in range(von, bis + 1):
        wort = ''.join(konsonanten[:i])
        vorzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        subprocess.call(["cver/arsch", wort],
                        stdout=DEVNULL, stderr=DEVNULL)
        sandwichzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        subprocess.call(["python3", "pyver/riddle_once.py", wort],
                        stdout=DEVNULL, stderr=DEVNULL)
        nachzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        zeitencpp.append(sandwichzeit - vorzeit)
        zeitenpy.append(nachzeit - sandwichzeit)
        print(f"{i}: (c++) {sandwichzeit - vorzeit} (py) {nachzeit - sandwichzeit}")

    datei = open("resonic/sonicsafter" + str(von) + "_" + str(bis) + ".csv", 'w', newline="")
    schreiber = csv.writer(datei, dialect="excel")
    schreiber.writerow(["wortlänge", "c++ zeit", "python zeit"])
    counter = 0
    for i in range(von, bis + 1):
        schreiber.writerow([i, zeitencpp[counter], zeitenpy[counter]])
        counter += 1
    datei.close()

    plt.plot(list(range(von, bis + 1)), zeitencpp, label="C++")
    plt.plot(list(range(von, bis + 1)), zeitenpy, label="Python")
    plt.legend(loc="upper left")
    plt.xticks(list(range(von, bis + 1)))
    plt.savefig("resonic/sonicsafter" + str(von) + "_" + str(bis) + ".png")
    plt.show()