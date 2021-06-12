edad = -7

if 0<edad<100:#concatenacion de operadores de asignacion
    # para que la condicion no admita valores negativos
    print('Edad es correcta')
else:
    print('Edad incorrecta')

salario_presidente = int(input('Introduce el salario de presidente: '))
print('Salario presidente: ',str(salario_presidente))

salario_director = int(input('Introduce el salario del director: '))
print('Salario director: ',str(salario_director))

salario_jefe_area = int(input('Introduce el salario del jefe de area: '))
print('Salario jefe de area: ',str(salario_jefe_area))

salario_administrativo = int(input('Introduce el salario del administrativo: '))
print('Salario administrativo: ',str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:# Tres operadores de comparacion concatenados, siempre se evalua de izquierda a derecha
    print('Todo funciona correctamente')
else: 
    print('Algo falla en esta empresa')