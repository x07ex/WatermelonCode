"""
2.- Dulces de Cumpleaños

Una mamá esta preocupada porque compró una cantidad de dulces, pero no sabe si es que será suficiente para todos los niños del cumpleaños de su hijo. Ella sabe lo importante que son los dulces para los niños, también ella sabe que si un niño o niña tiene más dulces que otro o otra el cumpleaños se arruinará. Por lo tanto, ella quiere saber si es que puede darle la misma cantidad de dulces a todos los niños.
"""

def _main(a: int, b: int) -> int:
    result = a / b % 1
    if result == 0:
        return a // b
    return -1

_main(10, 2) # Output: 2