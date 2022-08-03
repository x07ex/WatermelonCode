"""
16.- La pizza

Tu y tus amigos compran pizza juntos, tristemente la pizza tiene n-1 pedazos y ustedes son n personas (denotadas de 1 a n).
Para decidir quién no tendrá pizza propones el siguiente método: Primero se colocan en círculo de forma ascendente de 1 a n tal que depsués de n venga el 1. Depsués van pasando por el círculo partiendo desde la persona 1, y cada dos pasos la persona que esté en esa posición en el círculo saca un pedazo de pizza y sale del círculo. 
Siguen este proceso hasta que quede solo una persona que será la que no comerá pizza.
Tu tarea es simular este proceso para un n dado.
"""

def _main(n: int):
    n1 = [i + 1 for i in range(n)]
    array = []
    
    for x in n1:
        if x % 2 == 0: array.append(x)
    for x in n1:
        if x % 2 != 0: array.append(x)
    return " ".join(str(x) for x in array)

print(_main(7))