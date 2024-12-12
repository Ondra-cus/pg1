def dec_to_bin(cislo):
    """
    Převádí desetinné číslo (jako int nebo str) na jeho binární reprezentaci.

    Argumenty:
        cislo (int nebo str): Číslo k převodu.

    Návratová hodnota:
        str: Binární reprezentace čísla.
    """
    # Převedeme vstup na celé číslo
    cislo = int(cislo)

    # Pokud je číslo 0, vracíme "0"
    if cislo == 0:
        return "0"

    vysledek = ""

    # Provádíme převod na binární reprezentaci
    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek  # Zbytek přidáváme zleva
        cislo = cislo // 2

    return vysledek


def test_dec_to_bin():
    """Testovací funkce pro dec_to_bin."""
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    assert dec_to_bin(167) == "10100111"  # Test pro číslo 167


if __name__ == "__main__":
    print(dec_to_bin(120))
