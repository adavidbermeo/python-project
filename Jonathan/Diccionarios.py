#Los diccionarios funciona con la sintaxis clave:valor
midiccionario = {'Alemania':'Berlin','Francia':'Paris','Colombia':'Bogota','Reino Unido':'Londres'}

print(midiccionario['Francia'])#Pongo el nombre de la llave o key y me imprime el valor
print(midiccionario['Colombia'])

midiccionario['Italia']='Lisboa' #De esta forma agragamos elementos a un diccionario
print(midiccionario)

midiccionario['Italia']='Roma'# De esta forma modificamos el valor de una llave del diccionario
print(midiccionario)

del midiccionario['Reino Unido'] # La funcion del me permite borrar clave:valor de un diccionario
print(midiccionario)

midiccionario2 = {'Alemania':'Berlin',23:'Jordan','Pizza':10} # Se pueden hacer conbinaciones de diferentes tipos de datos en un diccionario
print(midiccionario2)

mitupla = ('Colombia','Francia','Reino Unido','Brasil')# Puedo crear una tupla con las claves para un diccionario
midiccionario3={mitupla[0]:'Bogota',mitupla[1]:'Paris',mitupla[2]:'Londres',mitupla[3]:'Rio de Janeiro'} 
print(midiccionario3) # Imprime el diccionario con su clave:valor

midiccionario4 = {23:'Jordan','Nombre':'Michael','Equipo':'Chicago','Anillos':(1991,1992,1993,1996,1997,1998)}# Se puede guardar una tupla de varios elementos a una clave
print(midiccionario4)
print(midiccionario4['Anillos'])

midiccionario4 = {23:'Jordan','Nombre':'Michael','Equipo':'Chicago','Anillos':{'Temporadas':(1991,1992,1993,1996,1997,1998)}}# Se puede crear un diccionario dentro de otro diccionario
#y el diccionario a sus vez tiene una tupla.    
print(midiccionario4['Anillos'])
print(midiccionario4.keys())# La funcion .keys() Me dice el nombre de todas las llaves de un diccionario
print(midiccionario4.values()) # La funcion .values() me dice los valores de todas las llaves de un diccionario

