"""
5.- Shopping List

Jansel quiere ayudar a su madre a hacer la lista de compras, para esto, deberá hacer un programa el cual le ayude a identificar que elemento x está en la posición i.
¿Porqué hace este programa?, bueno, básicamente es porque es tedioso tener una larga lista de compras, y más aún si se quiere buscar un elemento dentro de esta.
"""

def _main() -> str:
    longitud = int(input("Ingrese la longitud de la lista: "))
    lista = []
    for i in range(longitud):
        lista.append(input("Ingrese un elemento: "))
    posicion = int(input("Ingrese la posicion: "))
    print(f"El elemento en la posicion {posicion} es: {lista[posicion - 1]}")

_main()

