# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # ZDE NAPIŠTE VÁŠ KÓD
    
    seznam = []  # Seznam pro uchování výsledků
    for number in numbers:
        if number == 10:
            break  # break ukončí smyčku, když najde číslo 10
        if number > 5:
            seznam.append(number * 2)  # vynásobíme číslo 2 a dáme do seznamu , když je větší než 5
    return seznam


# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]
