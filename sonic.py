# sonic the hedgehog yk :)
# Geschwindigkeit messen von c++ und python

import string
import sys
import subprocess
from subprocess import DEVNULL
import resource

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

    zeiten = []
    for i in range(von, bis + 1):
        wort = ''.join(konsonanten[:i])
        vorzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        subprocess.call(["cver/arsch", wort],
                        stdout=DEVNULL, stderr=DEVNULL)
        sandwichzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        subprocess.call(["python3", "pyver/riddle_once.py", wort],
                        stdout=DEVNULL, stderr=DEVNULL)
        nachzeit = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        zeiten.append([sandwichzeit - vorzeit, nachzeit - sandwichzeit])
        print(f"{i}: (c++) {sandwichzeit - vorzeit} (py) {nachzeit - sandwichzeit}")