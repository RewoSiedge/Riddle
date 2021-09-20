# sonic the hedgehog yk :)
# Geschwindigkeit messen von c++ und python

import string
import sys
import subprocess

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

    for i in range(von, bis + 1):
        wort = konsonanten[:i]
        ergebnicpp = subprocess.check_output(["/usr/bin/time", "--format='%e'", "cver/arsch"], stderr=subprocess.STDOUT)
        ergebnipy = subprocess.check_output(["/usr/bin/time", "--format='%e'", "python", "pyver/riddle_once.py"], stderr=subprocess.STDOUT)
        print(f"{i}: (c++) {ergebniscpp[-5:-1]} (py) {ergebnispy[-5:-1]}")