# ----------------------------------------------------------------------
# B1. Python — CSV atskaite par servisiem
# ----------------------------------------------------------------------

# Saglabā ERROR rindu skaitu katram servisam CSV failā servisi.csv, ko var atvērt Excel ar latviešu burtiem. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pēc saglabāšanas izvadi rindu "Dati ierakstīti".

import csv

skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        if dalas[2] == "ERROR":
            serviss = dalas[3].rstrip(":")
            if serviss in skaits:
                skaits[serviss] = skaits[serviss] + 1
            else:
                skaits[serviss] = 1
                
with open("servisi.csv", "w", newline="", encoding="utf-8-sig") as f:
    r = csv.writer(f, delimiter=";")
    r.writerow(["Serviss", "Kļūdas"])
    for serviss, kludu_skaits in skaits.items():
        r.writerow([serviss, kludu_skaits])

# TODO: ieraksti skaits saturu failā servisi.csv
# Divas kolonnas: Serviss un Kļūdas
