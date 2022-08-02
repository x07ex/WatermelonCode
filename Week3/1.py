"""
15.- Helpful Maths  (i'm back people yahoo!)

Semana 3

Xenia, la matemática principiante, es una estudiante de tercer año en la escuela primaria. Ahora está aprendiendo la operación de suma.

El maestro ha escrito la suma de varios números. Los alumnos deben calcular la suma. Para facilitar el cálculo, la uma solo contiene los números 1, 2 y 3. Aún así, eso no es suficiente para Xenia. Ella solo está comenzando a contar, por lo que puede calcular una suma solo si los sumandos siguen en orden no decreciente. Por ejemplo, no puede calcular la suma 1 + 3 + 2 + 1 pero puede calcular las sumas 1 + 1 + 2 y 3 + 3.

Tienes la suma que estaba escrita en la pizarra. Reorganice las sumas e imprima la suma de tal manera que Xenia puede calcular la suma
"""

def _main() -> int:
    s = sorted(input().split("+"))
    n = ['+'.join(s[i:]) for i in range(len(s))]
    return n[0]

_main()