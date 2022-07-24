"""
7.- La suma de menor a mayor

Fran esta obsesionado con el ordenado de números, pero él no sabe programar. 
Entonces, le pide a ustedes realizar un código que reciba n números, y sumes los k valores más grandes.
"""

def _main() -> int:
    _, k = map(int, input().split()) # Recibiendo el numero de elementos y el numero de elementos a sumar
    numbers = list(map(int, input().split())) # Recibiendo los numeros
    numbers.sort() # Ordenando los numeros
    return sum(numbers[-k:]) # Sumando los k elementos mas grandes (-k: para que empiece desde el final)

_main()