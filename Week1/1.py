"""
Semana 1: “Esto es fácil ¿no?”

1.- Sum of Two Numbers

Matias es un genio de la matemática, es el más rápido de su clase a la hora de hacer las cuatro operaciones básicas de la aritmética. 
Su problema, es que se complica al momento de sumar dos números grandes. ¿Podrías Ayudarlo?
"""

def _main(a: int, b: int) -> int:
    max = round(10e4)
    # (if innecesariamente alargado, solo que asi se ve mas bonito)
    if (isinstance(a, int) and isinstance(b, int)):
        if (a > max or b > max):
            raise ValueError("Los numeros deben ser menores a 100000")
    return a + b

_main(2612, 8712) # Output: 11324 
