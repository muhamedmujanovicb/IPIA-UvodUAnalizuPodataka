# =============================================================
# ZADATAK 3: Excel - spajanje sheetova, obrada i export
# Uvod u analizu podataka - Vježbe, Sedmica 4
# =============================================================
# studenti.xlsx ima dva sheeta: "Grupa_A" i "Grupa_B" (po 20 studenata).
# Instalacija (ako već nije): pip install pandas openpyxl
#
# a) Učitaj oba sheeta u dva DataFrame-a.  Savjet: sheet_name="Grupa_A"
#
# b) Svakom dodaj kolonu "grupa" sa vrijednošću "A", odnosno "B".
#
# c) Spoji ih u jedan DataFrame.  Savjet: pd.concat([...], ignore_index=True)
#       očekivano: (40, 8)
#
# d) Dodaj kolone:
#       "prosjek" = (matematika + programiranje + statistika) / 3, zaokruženo na 2
#       "polozio" = True ako su sve tri ocjene >= 6
#       očekivano: (40, 10), položilo 25
#
# e) Spremi u "rezultati.xlsx" sa DVA sheeta:
#       "Svi"      - svih 40 studenata
#       "Polozili" - samo oni koji su položili (25)
#    Savjet:
#       with pd.ExcelWriter(putanja) as pisac:
#           df.to_excel(pisac, sheet_name="Svi", index=False)
#
# f) Pretvori sheet "Svi" iz rezultati.xlsx u "rezultati.csv" (index=False),
#    pa ga učitaj nazad i ispiši shape.  očekivano: (40, 10)
# =============================================================
import os
import pandas as pd
import openpyxl

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

FOLDER = os.path.dirname(os.path.abspath(__file__))
EXCEL = os.path.join(FOLDER, "studenti.xlsx")
IZLAZ_XLSX = os.path.join(FOLDER, "rezultati.xlsx")
IZLAZ_CSV = os.path.join(FOLDER, "rezultati.csv")

# a) TODO: učitaj Grupa_A i Grupa_B
grupa_b = pd.read_excel(EXCEL, sheet_name="Grupa_B")
print("Grupa B:", grupa_b.shape)
print(grupa_b.head(3))

grupa_a = pd.read_excel(EXCEL, sheet_name="Grupa_A")
print("Grupa A:", grupa_a.shape)
print(grupa_a.head(3))

# b) TODO: kolona "grupa"
grupa_a["grupa"] = "A"
grupa_b["grupa"] = "B"

# c) TODO: concat
sve = pd.concat([grupa_a, grupa_b], ignore_index=True)
print("Nakon concat:", sve.shape)          # (40, 7)
print(sve.tail(3))

# d) TODO: prosjek i polozio
sve["prosjek"] = ((sve["matematika"] + sve["programiranje"] + sve["statistika"]) / 3).round(2)
sve["polozio"] = (sve["matematika"] >= 6) & (sve["programiranje"] >= 6) & (sve["statistika"] >= 6)

print("Nakon dodavanja kolona:", sve.shape)  # očekivano: (40, 10)
print("Broj položenih:", sve["polozio"].sum()) # očekivano: 25

# e) TODO: ExcelWriter sa dva sheeta
with pd.ExcelWriter(IZLAZ_XLSX) as pisac:
    sve.to_excel(pisac, sheet_name="Svi", index=False)

    sve[sve["polozio"]].to_excel(pisac, sheet_name="Polozili", index=False)

print("Excel fajl sa dva sheeta uspješno sačuvan u:", IZLAZ_XLSX)

# f) TODO: Excel -> CSV i provjera
svi = pd.read_excel(IZLAZ_XLSX, sheet_name="Svi")
svi.to_csv(IZLAZ_CSV, index=False)
provjera = pd.read_csv(IZLAZ_CSV)
print("Nakon provjera:", provjera.shape)

print("Zadatak 3 - dopuni TODO dijelove.")
