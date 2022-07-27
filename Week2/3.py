"""
10.- Playing with Structures

Un amigo y tú están asistiendo a las clases de Watermelon, luego de las clases de stacks y queues tu amigo se siente un poco confundido. 
Este te dice que no entiende la diferencia entre una stack y una queue.
Tú, como buen amigo, 
quieres programar un código que reciba una secuencia de números y muestre el orden en que salgan tanto de una stack como de una queue.
"""

def _main(n: int, numbers: int) -> int:
    return (
        numbers[::-1]
        if n == len(numbers)
        else _main(n, numbers[:-1])
    )

_main(
    5,
    [2, 3, 3, 1, 4] # Output: [4, 1, 3, 3, 2]
)
