"""
3.- Size

A Emma, en su colegio, le han dado la tarea de calcular el tamaño de una cadena S, esto en teoría es muy fácil, pero a el le ha dado un poco de pereza, prefiere hacer un programa que le ayude en su tarea. ¿Puedes ayudarlo?
"""

def _main(string: str) -> int:
    # return len(string)
    count = 0
    for _ in string:
        count += 1
    return count

_main("I like watermelon code.") # Output: 23
