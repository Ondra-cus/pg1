import math

def je_prvocislo(cislo):
    """
    Funkce ověří, zda zadané číslo je prvočíslo, a vrátí True nebo False.
    Prvočíslo je takové číslo větší než 1, které není dělitelné žádným jiným číslem než 1 a samo sebou.
    """
    cislo = int(cislo)
    if cislo <= 1:
        return False
    for delitel in range(2, int(math.sqrt(cislo)) + 1):
        if cislo % delitel == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce vrátí seznam všech prvočísel v rozsahu od 2 do zadaného maxima včetně.
    """
    maximum = int(maximum)
    results = [i for i in range(2, maximum + 1) if je_prvocislo(i)]
    return results

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    print(f"Je číslo {cislo} prvočíslo? {je_prvocislo(cislo)}")
    prvocisla = vrat_prvocisla(cislo)
    print("Prvočísla mezi 1 a", cislo, "jsou:", prvocisla)
