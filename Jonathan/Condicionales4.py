# print('Programa de becas')

# distancia_escuela = int(input('Introduce la distancia a la escuala en Km: '))
# print(distancia_escuela)

# numero_hermanos = int(input('Introduce el numero de hermanos estudiando en la universidad: '))
# print(numero_hermanos)

# salario_familiar = int(input('Introduce el salario anual bruto: '))
# print(salario_familiar)

# if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:#si las dos primeras condiciones no se complen y la ultima si, se ejecuta el if,si no se cumplen las tres se ejecuta el else
#     print('Tienes derecho a beca')
# else:
#     print('No tienes derecho a beca')

print('Asignaturas optativas año 2021')
print('Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y Accesibilidad')
asignatura = input('Escribe la asignatura escogida: ')

if asignatura in ('Informatica grafica','Pruebas de software','Usabilidad y Accebilidad'):
    print('Asignatura elegida',asignatura)
else:
    print('La asignatura escogida no esta contemplada')

