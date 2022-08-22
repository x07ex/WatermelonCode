"""
14.-Maps (non geographics)

Tú eres el asistente de un profesor en la escuela y ella esta corrigiendo pruebas de alumnos. Cada alumno tiene multiples hojas de respuestas. Entonces la profesora quiere hacer Q consultas.
1 X Y: agrega el puntaje Y al estudiante con nombre X.
2 X: elimina el puntaje del estudiante con nombre X.
3 X: muestra por pantalla el puntaje del estudiante con nombre X. (Si X no tiene puntaje, entonces muestre por pantalla 0)
"""

def _main():
    x = []
    n = int(input("Ingresa la consulta").split(" "))
    for i in range(n):
        if (input[0] == "3"):
            alumno = x.find(alumno.name == input[1])
            print(alumno != None)
