def suma(): # Una funcion sin parametros, La principal utilidad de una funcion es reutilizar el codigo
    num1 = 5  
    num2 = 7
    print(num1+num2)

suma() # Llamado de la funcion

def suma2(num1,num2): # Funcion con parametros 
    print(num1 + num2)

suma2(10,2) # Se hace la llamada y se asignan los valores

suma2(11,25) # Se pueden modificar los valores asignados por parametro en cada llamada

suma2(13,13)

def resta(num1,num2): #Funcion con parametros que devuelve una variable (return)
    resultado = num1 - num2
    return resultado

print(resta(10,3))# Cuando una varible tiene un return se debe imprimir al hacer la llamada, para que se muestre por pantalla un resultado