"""
const alumnos = []
const n = Number(prompt("Ingresa la consulta").split(" "))
for (let i = 0; i < n; i++) {
    if (input[0] == "3") {
        const alumno = alumnos.find(alumno => alumno.name == input[1])
        console.log(alumno != undefined ? alumno.points : 0)
    } else if (input[0] == "1") {
        const index = alumnos.findIndex(alumno => alumno.name == input[1])
        if (index == -1) alumnos.push({ name: input[1], points: input[2]})
        else alumnos[index].points += Number(input[2])
    } else if (input[0] == "2") {
        const index = alumnos.findIndex(alumno => alumno.name == input[1])
        delete alumnos[index]
    } else {
        console.log("Opcion no valida)
    }
}
"""

def _main():
    x = []
    n = int(input("Ingresa la consulta").split(" "))
    for i in range(n):
        if (input[0] == "3"):
            alumno = x.find(alumno.name == input[1])
            print(alumno != None)