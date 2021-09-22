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
        wort = ''.join(konsonanten[:i])
        ergebnicpp = subprocess.check_output(["gtime", "--format='%e'", "cver/arsch", wort], stderr=subprocess.STDOUT)
        ergebnipy = subprocess.check_output(["gtime", "--format='%e'", "python3", "pyver/riddle_once.py", wort], stderr=subprocess.STDOUT)
        print(f"{i}: (c++) {ergebnicpp[-6:-2].decode('utf-8')} (py) {ergebnipy[-6:-2].decode('utf-8')}")