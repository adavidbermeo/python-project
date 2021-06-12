# Bucles anidados 
# utilizamos bucles for

#¿Que es un bucle anidado?
#Se habla de bucles anidados cuando un bucle se encuentra en el bloque de instrucciones de otro bloque.
#Al bucle que se encuentra dentro del otro se le puede denominar bucle interior o bucle interno
#Los bucles pueden tener cualquier nivel de anidamiento (un bucle dentro de otro bucle dentro de un tercero, etc.).

# Ejemplo 

#for i in range(1,4):        #por cada valor de i que vaya tomando, el valor de j va a ir iterando 3 veces
    #Es decir mientras i valga 1, j va a valer 1,2,3. Posteriormente volveremos al primer bucle
    #i valdrá 2 y j vovlerá a valer 1,2,3 
    #for j in range (1,4):   #por cada iteración de i van a ver 3 iteraciones de j
        #print(i,j)

#Ejemplo, crear una baraja con bucles añadiendo las cartas a una lista mediante bucles for

#baraja = ["A de oros", "2 de oros",...] nos tardariamos mucho, para eso está el for

tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"] 

palos = ["oros", "copas", "espadas", "bastos"]

baraja = []

#tengo creadas dos listas, ahora en una tercera la dejo vacía pues allí es donde se irán creando las cartas

#Ahora va la creación del bucle

for t in tantos:
    for p in palos:
        carta = "{} de {}".format(t,p)
        baraja.append(carta)

#print(baraja)

#¿ Que fue lo que se hizo?

#por cada t (tanto) se me deben generar 4 cartas 

"ahora si quiero que quede mas bonita la impresión puedo arreglarlo también con un bucle for"

for i in range(0, 40, 4):   #un bucle for desde el cero hasta la carta 40 con salto 4
    print("{} {} {} {}".format(baraja[i], baraja[i+1], baraja[i+2], baraja[i+3]))
#un print con 4 grupos de llaves con las que les he pasado el indice i de la baraja, el i+1, i+2 y el i+3


