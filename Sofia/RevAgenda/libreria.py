import os

def limpiar():
  if os.name == "posix":
    os.system ("clear")
  else:
    if os.name == "ce" or os.name == "nt" or os.name == "dos":
      os.system ("cls")

def color(col):
  if (col=="negro"):
    # BLACK = '\033[30m'
    col1=  '\033[30m'
  else:
    if (col=="rojo"):
      # RED = '\033[31m'
      col1= '\033[31m'
    else:
      if(col=="verde"):
        # GREEN = '\033[32m'
        col1= '\033[32m'
      else:
        if (col=="amarillo"):
          # YELLOW = '\033[33m'
          col1= '\033[33m'
        else:
          if (col=="azul"):
            # BLUE = '\033[34m'
            col1 = '\033[34m'
          else:
            if (col =="magenta"):
              # MAGENTA = '\033[35m'
              col1 =  '\033[35m'
            else:
              if (col=="cyan"):
                # CYAN = '\033[36m'
                col1 =  '\033[36m'
              else:
                if  (col== "blanco"):
                  # WHITE = '\033[37m'
                  col1= '\033[37m'
                else:
                  if (col=="nada"):
                    # RESET = '\033[39m'
                    col1=  '\033[39m'
                  else:
                    col1=  '\033[39m'
  return col1

def mensaje(col,texto):
  #print(color("rojo")+texto+color("nada"))
  print(color(col)+texto+color("nada"))

def presentacion():
  print(color("azul")+"Logo de la empresa"+color("nada"))

def salir():
  print("Salir")

def pausa(col,texto):
  x=color(col)+texto+color("nada")
  p=input(x)