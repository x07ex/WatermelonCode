"""
4.- Concatenate a String

Solo es concatenar un string, no tiene mucho misterio.
"""

def _main(text: str) -> str:
    a, b = text.split(" ")
    return f"{a} {b}"

_main("watermelon code") # Output: watermelon code