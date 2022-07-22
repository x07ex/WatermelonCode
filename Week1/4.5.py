"""
4.5? Counting Numbers

Este desafío es un "desafío", y es para la gente que está encontrando fácil estos y quiere algo un poco más tipo semana 3/ semana 4 de esta maratón :p
Su tarea es contar el número de enteros entre a y b donde no hay dos dígitos adyacentes iguales
Restricciones:
0 ≤ a ≤ b ≤ 1018

* Este desafio no suma puntos, solo es un sneak peek de la ultima semana. *
Gracias por la logica a: @zNareaк
"""

def _main() -> int:
    n1, n2 = map(int, input().split(" "))
    c = 0 # contador
    for i in range(n1, n2 + 1): # iterar entre n1 y n2
        p = list(str(i)) # convertir a string
        b = 1 # bandera
        for k in range(len(p) - 1): # iterar entre los digitos
            if p[k] == p[k + 1]: # si son iguales
                b = 0 # bandera = 0
        if b: # si bandera = 1
            c += 1 # sumar al contador
    return c # retornar contador

_main()