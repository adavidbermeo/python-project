milista = ['Maria','Pepe','Gladys','Juan']

print(milista) ## La sintaxis para imprimir una lista completa 
print(milista[:])# La sintaxis para imprimir una lista completa 

print(milista[2]) # Para acceder a un solo elemento de una lista se pone el indice entre corchetes

print(milista[0:3]) # Para acceder a una porcion de una lista iniciando desde el indice 0 hasta el 2 de una lista, con dicha nomenclatura declarada [0:3]

print(milista[2:]) # Para acceder desde la posicion en este caso 2 hasta el final de la lista

milista.append('Jonathan') # se utiliza la funcion .append para agregar un elemento al fianl de una lista

milista.extend([10,4.66,'Jesus',True]) # Se utiliza la funcion .extend para agregar uno o mas elementos al final de una lista

milista.insert(1,'Jenifer') 
'''Se utiliza la funcion .insert para agregar un alemento en la posicion que queramos en este ejemplo seria la posicion 1, la cual se declara dentro de
los parentesis'''

milista.remove(4.66) # Se utiliza la funcion .remove para eliminar un elemento de una lista

milista.pop() # Esta funcion pop() elimina el ultimo elemento de una lista

milista2 = ['Violeta',26,'Aurelio'] # Creo otra lista

milista3 = milista+milista2 # Concateno dos listas con el operador suma(+)

milista4 = [10,'Hola','Mundo']*3 # En este caso me remite la lista 3 veces o las veces que yo quiera utilizando el opelador multiplicar(*)

print(milista.index('Jonathan')) # La funcion index me devuelve el indice del elemento que yo le pida de una lista

print('Gladys' in milista)# Si el elemento existe dentro de una lista mi imprime True, de los contrario False

print(milista)

print(milista3)

print(milista4)