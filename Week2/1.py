"""
8.- Grilla perfecta

A Andrea le encantan los arreglos bidimensionales, y ha inventado un juego para jugar con sus amigas, en esté se tendrá que identificar si una grilla es perfecta, ¿Cuándo una grilla es perfecta? Cuando tiene números 1 cruzando la matriz diagonalmente hacia un lado o otro.
Se sabe que la matriz siempre será de un largo y alto impar

Tu tarea es crear un programa el cuál identifique si la matriz es perfecta.
"""

def _main(num: int, matrix: tuple or list) -> str:
    matrix = matrix.split('\n')
    if num % 2 != 0 and len(matrix[0]) % 2 != 0:
        return f"{matrix}\nYes"
    else:
        return f"{matrix}\nNo"

_main(3, '\n'.join(['1 0 0', '0 0 1', '0 1 0']))
