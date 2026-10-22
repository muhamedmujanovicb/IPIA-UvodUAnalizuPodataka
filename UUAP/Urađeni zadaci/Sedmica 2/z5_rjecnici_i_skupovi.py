# =============================================================
# ZADATAK 5: Rječnici i skupovi - "Rođendani u grupi"  (~5 minuta)
# Veza sa predavanjem: Birthday Paradox
# =============================================================

rodjendani = [
    "03-14", "07-22", "11-05", "03-14", "01-30", "09-09",
    "12-25", "07-22", "05-17", "02-28", "10-10", "07-22",
    "04-01", "08-15", "06-06", "11-05", "03-03", "09-18",
]

# a) Koliko je ukupno rođendana u listi?
# TODO

counter = 0
for i in range(1, len(rodjendani), 1):
    counter += 1
print(counter)

# b) Koliko ima JEDINSTVENIH rođendana?  Savjet: set()
# TODO
jedinstveni = set(rodjendani)
print(len(jedinstveni))

# c) Postoje li duplikati? Ispiši True/False.
# TODO
duplikati = []

for i in rodjendani:
    if i in rodjendani:
        duplikati.append(i)

if(len(duplikati) > 0): print("True")
else: print("False")
# d) Pomoću rječnika (ili Counter-a) prebroj koliko se puta
#    pojavljuje svaki datum i ispiši SAMO datume koji se ponavljaju.
#    Očekivano:  03-14 -> 2 puta,  07-22 -> 3 puta,  11-05 -> 2 puta
# TODO
counter = 0

for i in range(1, len(rodjendani), 1):
    if(rodjendani[i] in duplikati):
        for j in range(1, len(duplikati), 1):
            if(rodjendani[i] == duplikati[j]):
                counter +=1
    print(f"Duplikat {rodjendani[i]} se ponavlja {counter} puta")
    counter = 0

# e) BONUS: Koliko je studenata rođeno u martu (mjesec "03")?
#    Savjet: datum[:2] daje mjesec
# TODO
