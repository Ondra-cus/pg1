def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.

    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    start = figurka["pozice"]
    cil_r, cil_s = cilova_pozice


    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False


    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "pěšec":
        if start[0] == 2 and cil_r == 4 and start[1] == cil_s and (start[0] + 1, start[1]) not in obsazene_pozice:
            return True
        if cil_r == start[0] + 1 and start[1] == cil_s:
            return True
    elif typ == "jezdec":
        if (abs(cil_r - start[0]), abs(cil_s - start[1])) in [(2, 1), (1, 2)]:
            return True
    elif typ == "věž":
        if cil_r == start[0] or cil_s == start[1]:
            if all((r, s) not in obsazene_pozice for r in range(min(start[0], cil_r) + 1, max(start[0], cil_r)) for s in range(min(start[1], cil_s) + 1, max(start[1], cil_s))):
                return True
    elif typ == "střelec":
        if abs(cil_r - start[0]) == abs(cil_s - start[1]):
            if all((start[0] + i, start[1] + j) not in obsazene_pozice for i, j in zip(range(1, abs(cil_r - start[0])), range(1, abs(cil_s - start[1])))):
                return True
    elif typ == "dáma":
        if cil_r == start[0] or cil_s == start[1] or abs(cil_r - start[0]) == abs(cil_s - start[1]):
            if all((r, s) not in obsazene_pozice for r in range(min(start[0], cil_r) + 1, max(start[0], cil_r)) for s in range(min(start[1], cil_s) + 1, max(start[1], cil_s))):
                return True
    elif typ == "král":
        if abs(cil_r - start[0]) <= 1 and abs(cil_s - start[1]) <= 1:
            return True
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}



    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True