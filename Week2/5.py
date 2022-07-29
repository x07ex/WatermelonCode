"""
12.- Is...?

Tu tarea será hacer un programa que reciba un string S, el programa debe identificar si está en lowercase, o uppercase, además de esto, deberá cambiarlo a su contrario, pero sin usar los upper() y lower() de dicho lenguaje de programación, con esto me refiero a que esta prohibido utilizar los métodos predefinidos en el lenguaje a usar.
S solo puede ser lowercase o UPPERCASE, no mixto.
"""

def toUpperCase(txt: str) -> str:
    newText = ""
    for x in txt:
        if ord(x) > 96 \
            and ord(x) < 123:
                newText += chr(ord(x) - 32)
        else:
            newText += x
    return newText

def toLowerCase(txt: str) -> str:
    newText = ""
    for x in txt:
        if ord(x) > 64 \
            and ord(x) < 91:
                newText += chr(ord(x) + 32)
        else:
            newText += x
    return newText

def _main(txt: str) -> str:
    if txt.islower():
        print("LowerCase\n" + toUpperCase(txt))
    else:
        print("UpperCase\n" + toLowerCase(txt))

_main("watermelon")
