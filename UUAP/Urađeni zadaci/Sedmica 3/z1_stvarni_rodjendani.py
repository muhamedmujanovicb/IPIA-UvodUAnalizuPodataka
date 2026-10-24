# =============================================================
# ZADATAK 1: Stvarni rođendani - da li se paradoks potvrdio?
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
# U fajlu real_birthdays.txt su rođendani studenata (format DD-MM).
# Provjeri da li u našoj grupi postoje isti rođendani i uporedi
# rezultat sa teorijom (Birthday Paradox).
# =============================================================
import os
from collections import Counter

# Putanja do fajla koji se nalazi u istom folderu kao ova skripta
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")

# --- Učitavanje ---------------------------------------------
# Učitaj sve datume iz fajla u listu datumi.
# Savjet: with open(FAJL, "r", encoding="utf-8") as f:
#         strip() i preskoči prazne redove
datumi = []
# TODO
with open(FAJL, "r", encoding = "utf-8") as f:
    redovi = f.readlines()
    for red in redovi:
        red = red.strip()
        if red == "":
            continue
        datumi.append(red)

print(datumi)

# a) Koliko je ukupno rođendana?            (očekivano: 38)
# TODO

print(f"Ukupan broj: {len(datumi)}")


# b) Koliko je JEDINSTVENIH rođendana?      (očekivano: 34)
#    Savjet: set()
# TODO

datumiuniq = datumi
output = []
for i in datumiuniq:
    if i not in output:
        output.append(i)

print(f"Jedinstvenih: {len(output)}")

# c) Postoje li duplikati? Ispiši True/False.
# TODO
datumidup = datumi
for n in datumi:
    if n in datumidup:
        print("True")
        break

# d) Koji se datumi ponavljaju? Ispiši ih SORTIRANO, npr:
#       03-01 -> 2 puta
#    Savjet: Counter(datumi), pa sorted(...)
# TODO

datumrep = datumi
counter = Counter(datumrep)
for value, count in sorted(counter.items()):
    if count > 1:
        print(f"{value} se ponavlja {count} puta")


# e) Uporedi sa teorijom.
#    Vjerovatnoća da u grupi od n osoba NIKO nema isti rođendan je:
#       (365/365) * (364/365) * (363/365) * ... * ((365-n+1)/365)
#    Vjerovatnoća poklapanja = 1 - to.
#    Napiši funkciju i ispiši:
#       Teorijska vjerovatnoća za 38 osoba: 86.4%
def vjerovatnoca_poklapanja(n):
    # TODO
    for n in range(1, n, 1):
        prob = ((365-n+1)/365)
    print(prob)

vjerovatnoca_poklapanja(38)

# TODO: ispiši rezultat za len(datumi) osoba


# BONUS: Koliko je rođendana u svakom mjesecu?
#    Savjet: mjesec je dio iza crtice -> datum.split("-")[1]
# TODO
