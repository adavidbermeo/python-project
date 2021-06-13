# Importacion
import libreria as lib

def menu():
  lib.presentacion()
  print("    ***   M E N U   ***")
  print("        A G E N D A")
  print("    1. Adicionar (Ingresar)")
  print("    2. Consultar")
  print("    3. Eliminar")
  print("    4. Actualizar")
  print("    5. Listar")
  print("    6. Salir")

def adicionar(codigo,nombres,apellidos):
  lib.limpiar()
  print("Adicionar...")
  cod=input("Codigo : ")
  if (cod in codigo):
    lib.pausa("cyan","Codigo ya Existe, Digite <Enter> para continuar...")
  else:
    nom=input("Nombre : ")
    ape=input("Apellidos : ")
    codigo.append(cod)
    nombres.append(nom)
    apellidos.append(ape)

def consultar(codigo,nombres,apellidos):
  lib.limpiar()
  print("Consultar")
  cod=input("Codigo : ")
  if (cod in codigo):
    idx=codigo.index(cod)
    print("nombre : ",nombres[idx])
    print("Apellidos : ",apellidos[idx])
    lib.pausa("cyan","Digite <Enter> paa continuar...")
  else:
    lib.pausa("cyan","codigo No existe ... , Digite <Enter> paa continuar...")


def eliminar(codigo,nombres,apellidos):
  lib.limpiar()
  print("Eliminar")
  cod=input("Codigo : ")
  if (cod in codigo):
    idx=codigo.index(cod)
    print("nombre : ",nombres[idx])
    print("Apellidos : ",apellidos[idx])
    respuesta=input("Seguro de Eliminar S/N : ")
    if (respuesta=="S" or respuesta=="s"):
      codigo.pop(idx)
      nombres.pop(idx)
      apellidos.pop(idx)
    else:
      lib.pausa("cyan","codigo No Eliminado ... , Digite <Enter> para continuar...")
  else:
    lib.pausa("cyan","codigo No existe ... , Digite <Enter> paa continuar...")


def actualizar(codigo,nombres,apellidos):
  lib.limpiar()
  print("Actualizar")
  cod=input("Codigo : ")
  if (cod in codigo):
    idx=codigo.index(cod)
    txt_nombre="Nombres : "+nombres[idx]+" Nombres Nuevos : "
    txt_apellido="Apellidos : "+apellidos[idx]+" Apellidos Nuevos : "
    nom=input(txt_nombre)
    ape=input(txt_apellido)
    nombres[idx]=nom
    apellidos[idx]=ape
  else:
    lib.pausa("cyan","codigo No existe ... , Digite <Enter> paa continuar...")

def listar(codigo,nombres,apellidos):
  print("Listar")
  for i in range (len(codigo)):
    print(codigo[i]," ",nombres[i]," ",apellidos[i])
  
  lib.pausa("cyan","Digite <Enter> paa continuar...")


