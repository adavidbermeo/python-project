# Bucle determinado 

## El bucle for se utiliza para recorrer los elementos de un objeto iterable 
# (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código

# # Python
# for iterable in elemento:

#     # Hacer algo con el element

## Iterar una lista

lista = ['Juan','Sofia','Harold','Angel']

edad = {'Sofia':[25,12,14,34],'Angel':(20,3,5,6,8),'Harold':23,'Sebastian':18}

for llave,valor in edad.items():# en la primera ejecucion i=1 y ejecuta lo que esta dentro del bucle, de esa forma para esta declaracion del for se ejecuta 3 veces y se imprime hola tres veces 
    print(llave)
    print(valor)

#numero = int(input('Ingrese un numero'))
#lista2=[1,2,3,4,5,6]
for iterable in range(1,5):
    print(iterable)

# for iterador in ['Hola','Buenas tardes','Buenos dias','Buenas noches']: # De esta forma imprime los valores dentro de la lista
#     print(iterador)


# for i in range(5):
#     print(i)
