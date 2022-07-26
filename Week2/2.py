"""
9.- No repetidos

Teo quiere encontrar la maneral de anular los números repetidos en una lista, 
para ello decide hacer un programa para seguir con su investigación.
"""

def _main() -> int:
    _ = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(set(numbers))
    print(*numbers, sep = " ")

_main()