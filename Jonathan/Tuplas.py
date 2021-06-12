mitupla = ('Juan',16,3,1998) # Las tuplas son inmutables

milista = list(mitupla) # Funcion para convertir una tupla a lista 

print(mitupla[2]) # Para acceder al elemento de una tupla

milista2 = ['Sofia','Harold','Angel',10]

mitupla2 = tuple(milista2) #Funcion para convertir una lista a tupla

print(mitupla2)

print(mitupla.count(3))# La funcion .count me dice cuantas veces esta dentro de una tupla un elemento en este ejemplo decimos 3 pero tambien puede ser 'Juan'

print(len(mitupla2)) # La funcion len() me dice la cantidad de elemento de una tupla o una lista

## Se puede asiganr variables a los elementos de una tupla, se debe tener en cuenta el orden

Nombre, Dia, Mes, Año = mitupla

print(Nombre)
print(Año) #No importa el orden en el que lo imprima
print(Dia)
print(Mes)