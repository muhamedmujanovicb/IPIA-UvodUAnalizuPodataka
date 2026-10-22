# =============================================================
# ZADATAK 4: Funkcije   (~8 minuta)
# =============================================================

# a) Napiši funkciju prosjek(lista) koja vraća prosjek brojeva u listi.
#    Ako je lista prazna, neka vrati 0.
def prosjek(lista):
    # TODO
    if(not lista):
        return 0
    else:
        return sum(lista) / len(lista)
    pass


# b) Napiši funkciju je_paran(n) koja vraća True ako je n paran,
#    a False ako nije.
def je_paran(n):
    # TODO
    if(n%2==0):
        return True
    else:
        return False
    pass


# c) Napiši funkciju ocjena(bodovi) koja vraća ocjenu prema
#    pravilima iz Zadatka 3a.
def ocjena(bb):
    # TODO
    if (bb <= 54):
        return print("5")
    elif (bb >= 55 and bb <= 64):
        return print("6")
    elif (bb >= 65 and bb <= 74):
        return print("7")
    elif (bb >= 75 and bb <= 84):
        return print("8")
    elif (bb >= 85 and bb <= 94):
        return print("9")
    elif (bb >= 95):
        return print("10")
    pass


# d) Napiši funkciju samo_parni(lista) koja vraća NOVU listu
#    samo sa parnim brojevima. Iskoristi funkciju je_paran!
def samo_parni(lista):
    nova_lista = []
    # TODO
    for i in range(1,len(lista),1):
        if(je_paran(lista[i])):
            nova_lista.append(lista[i])
    return print(nova_lista)
    pass


# --- Testiranje (ne mijenjaj) -------------------------------
print(prosjek([8, 9, 10]))          # 9.0
print(prosjek([]))                  # 0
print(je_paran(4), je_paran(7))     # True False
print(ocjena(50), ocjena(78), ocjena(100))   # 5 8 10
print(samo_parni([1, 2, 3, 4, 5, 6]))        # [2, 4, 6]
