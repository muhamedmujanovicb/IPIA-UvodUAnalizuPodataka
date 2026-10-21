# =============================================================
# ZADATAK 1: Varijable, unos i aritmetika   (~7 minuta)
# =============================================================

# a) Napiši program koji pita korisnika za ime i godinu rođenja,
#    a zatim ispiše poruku oblika:
#       "Zdravo Amra, ove godine puniš 21, a 2030. ćeš imati 25 godina."
#    Savjet: input() vraća tekst -> koristi int()

TRENUTNA_GODINA = 2026

# TODO: tvoj kod ovdje
print("Unesite vaše ime i godinu rođejna:")
print("Ime:")
ime = input()
print("Godina rodjenja:")
godina_rodjenja = input()

print(f"Zdravo {ime}, ove godine punis {(2026-int(godina_rodjenja))+1} a 2030 ces imati {2030-int(godina_rodjenja)}")

# b) Korisnik unese broj sekundi (npr. 3725).
#    Ispiši koliko je to sati, minuta i sekundi:
#       "3725 s = 1 h 2 min 5 s"
#    Savjet: koristi // (cjelobrojno dijeljenje) i % (ostatak)

# TODO: tvoj kod ovdje

print("Unesite broj sekundi:")
broj_sekundi = input()
print("Pretvorene vrijednosti:")
print(f"Sati {int(broj_sekundi)//3600} Minute {int(broj_sekundi)//60} Sekunde {int(broj_sekundi)%60}")
