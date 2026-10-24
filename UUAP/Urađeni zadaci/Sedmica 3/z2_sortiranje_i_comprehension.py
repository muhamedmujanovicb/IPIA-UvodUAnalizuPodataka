# =============================================================
# ZADATAK 2: Sortiranje, list comprehension, zip, enumerate, random
# Uvod u analizu podataka - Vježbe, Sedmica 3
# =============================================================
import os
import random

studenti = ["Amra", "Emir", "Lejla", "Tarik", "Ana"]
bodovi = [78, 92, 65, 88, 92]

# a) Pomoću zip() napravi listu parova (ime, bodovi) i ispiši
#    svaki par u obliku:   Amra: 78
# TODO


for student, bod in zip(studenti, bodovi):
    print(f"Ime: {student} - bodovi: {bodovi}")

# b) Sortiraj parove po bodovima OPADAJUĆE i ispiši rang listu
#    pomoću enumerate(..., start=1):
#       1. Emir - 92
#       2. Ana - 92
#       ...
#    Savjet: sorted(parovi, key=lambda p: p[1], reverse=True)
# TODO

parovi = list(zip(studenti, bodovi))
sortirani_parovi = sorted(parovi, key=lambda p: p[1], reverse=True)

for i, (ime, bod) in enumerate(sortirani_parovi, start=1):
    print(f"{i} . {ime} - {bod}")

# c) List comprehension: lista imena studenata sa 80 ili više bodova.
#    Očekivano: ['Emir', 'Tarik', 'Ana']
# TODO

for i, (ime, bod) in enumerate(sortirani_parovi, start=1):
    if(bod >= 80):
        print(f"{ime}")


# d) Iz fajla real_birthdays.txt (format DD-MM) napravi pomoću
#    list comprehension-a listu MJESECI kao brojeve (int),
#    a zatim ispiši sortirane jedinstvene mjesece.
#    Očekivano: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
FAJL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_birthdays.txt")
# TODO

with open(FAJL, "r", encoding="utf-8") as f:
    redovi = f.readlines();

datumi = []
for red in redovi:
    red = red.strip()
    if red == "":
        continue
    datumi.append(red)

mjeseci = [len(datumi)]

for i in range(len(datumi)):
    datum = datumi[i]
    dan, mjesec = datum.split("-")
    mjeseci.append(int(mjesec))

mjeseci.sort()
print(set(mjeseci))

# e) random: postavi random.seed(42), pa
#    - nasumično izaberi studenta koji odgovara (random.choice)
#    - napravi KOPIJU liste studenti i promiješaj je (random.shuffle)
#      -> to je redoslijed prezentacija
# TODO

random.seed(42)

print("random student", random.choice(studenti))

rstudenti = studenti.copy()
random.shuffle(rstudenti)
print(rstudenti)
