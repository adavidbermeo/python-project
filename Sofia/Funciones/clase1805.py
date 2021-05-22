# import
import math as m
from google.colab import output
# funciones
def menu():
  print("** M E N U **")
  print("1. Cuadrado")
  print("2. Rectangulo")
  print("3. Triangulo")
  print("4. Circulo")
  print("5. Salir")

def cuadrado():
  output.clear
  print("Área del cuadrado")
  lado=float(input("Digite el lado del cuadrado:"))
  area=lado*lado
  print("El área del cuadrado es: ", area)

def rectangulo():
  output.clear
  print("Área del rectangulo")
  base=float(input("Digite la base del rectangulo"))
  altura=float(input("Digite la altura del rectangulo"))
  area=base*altura
  print("El área del rectangulo es: ", area)

def triangulo():
  output.clear
  print("Área del triangulo")
  base=float(input("Digite la base del rectangulo"))
  altura=float(input("Digite la altura del rectangulo"))
  area=(base*altura)/2
  print("El área del triangulo es: ", area)

def circulo():
  output.clear
  print("Área de circulo")
  radio=float(input("Digite el radio del circulo: "))
  area=m.pi*(pow(radio,2))
  print("El área del circulo es: ", area)

def salir():
  print("Hasta la proxima") 


# principal
menu()
opcion=input("Digite la opción: ")
if (opcion=="1"):
  cuadrado()
else:
  if (opcion=="2"): 
    rectangulo()
  else:
    if (opcion=="3"):
      triangulo()
    else:
      if (opcion=="4"):
        circulo()
      else:
        if (opcion=="5"):
          salir()
