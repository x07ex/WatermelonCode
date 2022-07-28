"""
11.- ASCII Code

Los valores ASCII de las letras mínuculas en inglés a, b, …, z son 97, 98 …, 122 en ese orden.
Dado un entero N entre 97 y 122, muestre por pantalla la letra correspondiente cual valor ASCII es N.
"""

def _main(num: int) -> str:
    # return chr(num)
    abc = "abcdefghijklmnopqrstuvwxyz"
    return abc[num - 97] if 97 <= num <= 122 \
        else "[Invalid] ASCII code, range(97, 122)"    

_main(97)