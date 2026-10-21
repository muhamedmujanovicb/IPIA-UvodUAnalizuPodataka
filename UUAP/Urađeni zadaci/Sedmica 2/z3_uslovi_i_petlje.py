# =============================================================
# ZADATAK 3: Uslovi i petlje   (~10 minuta)
# =============================================================
import random

# a) Korisnik unese broj bodova (0-100). Ispiši ocjenu:
#      0-54 -> 5,  55-64 -> 6,  65-74 -> 7,
#      75-84 -> 8, 85-94 -> 9,  95-100 -> 10
# TODO

print("Unesi broj bodova 0-100")
bb = int(input())
if(bb <=54): print("5")
elif(bb >= 55 and bb <=64): print("6")
elif(bb >= 65 and bb <=74): print("7")
elif(bb >= 75 and bb <=84): print("8")
elif(bb >= 85 and bb <=94): print("9")
elif(bb >= 95): print("10")

# b) Pomoću for petlje izračunaj sumu svih PARNIH brojeva od 1 do 100.
#    (Rezultat treba biti 2550)
# TODO
sum = 0
for i in range(1, 101, 1):
    if(i % 2 == 0):
        sum += i
print(sum)

# c) MINI IGRA "Pogodi broj"
#    Računar zamisli broj od 1 do 20 (već napisano ispod).
#    Pomoću while petlje traži od korisnika da pogađa dok ne pogodi.
#    Nakon svakog pokušaja ispiši "Više!" ili "Manje!".
#    Na kraju ispiši iz koliko pokušaja je pogodio.
tajni_broj = random.randint(1, 20)
# TODO
counter = 0
pogodio = 0
while (pogodio == 0):
    counter += 1
    print("Pogodi broj")
    broj = int(input())
    if(broj == tajni_broj):
        print(f"Pogodio si iz {counter} pokusaja")
        pogodio == 1
        break
    elif(broj < tajni_broj):
        print("Vise")
    elif(broj > tajni_broj):
        print("Manje")
