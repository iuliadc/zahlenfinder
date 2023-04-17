import re

def zahlen_finder(text_datei):
    with open(text_datei, "r") as input:
        dokument = input.read()
    zahlen_liste = re.findall(r"\b\d{1,3}(?:(?:\.\d{3})*)?(?:,\d+)?", dokument)
    with open("extrahierte_zahlen.txt", "w") as output:
        for zahl in zahlen_liste:
            output.write(zahl)
            output.write("\n")

dateiname = input("Bitte den Dateipfad samt Dateinamen eingeben: ")
zahlen_finder(dateiname)