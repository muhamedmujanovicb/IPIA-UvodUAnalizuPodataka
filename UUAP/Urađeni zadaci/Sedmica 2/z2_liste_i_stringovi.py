# =============================================================
# ZADATAK 2: Liste i stringovi   (~7 minuta)
# =============================================================

ocjene = [8, 6, 10, 7, 9, 6, 8]

# a) Ispiši prvu i zadnju ocjenu.
# TODO
print("a)")
print(ocjene[0])
print(ocjene[6])


# b) Ispiši prve tri ocjene (koristi rezanje / slicing).
# TODO
print("b)")
print(ocjene[:3])


# c) Student je dobio još jednu ocjenu: 10. Dodaj je u listu.
# TODO
print("c)")
ocjene.append(10)
print(ocjene)

# d) Izračunaj i ispiši prosjek ocjena na 2 decimale.
#    Savjet: sum() i len()
# TODO
print("d)")
prosjek = sum(ocjene) / len(ocjene)
print(prosjek)

# e) Ispiši da li student ima ocjenu 6 (True/False).
# TODO
print("e)")
if(ocjene.__contains__(6)):
    print("true")

# f) Zadana je rečenica. Ispiši koliko ima riječi
#    i koja je najduža riječ.
#    Savjet: split(), a za najdužu riječ max(rijeci, key=len)
recenica = "analiza podataka pomaže da donosimo bolje odluke"
# TODO
print("f)")
rijeci = recenica.split()
print(len(rijeci))

print(max(rijeci,key=len))