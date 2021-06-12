nota_alumno = int(input('Ingrese la nota del alumno: '))

def evaluacion(nota):
    valoracion = 'Aprobado'
    if nota < 5:
        valoracion = 'Reprobado'
    return valoracion

print(evaluacion(nota_alumno))
