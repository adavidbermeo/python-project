#Importaciones
import libreria as lib
import agenda as age
#Constantes

#Estructura de datos
#
codigo=[]
nombres=[]
apellidos=[]
celular=[]
# lib.presentacion()
seguirmenu=True
while (seguirmenu):
  lib.limpiar()
  age.menu()
  opcion = input("     Opcion ==> :")
  if (opcion=="1"):
    age.adicionar(codigo,nombres,apellidos)
  else:
    if (opcion == "2"):
      age.consultar(codigo,nombres,apellidos)
    else:
      if (opcion =="3"):
        age.eliminar(codigo,nombres,apellidos)
      else:
        if (opcion =="4"):
          age.actualizar(codigo,nombres,apellidos)
        else:
          if (opcion=="5"):
            age.listar(codigo,nombres,apellidos)
          else:
            if (opcion=="6"):
              lib.salir()
              break
            else:
              lib.mensaje("rojo","Valor fuera de rango ... ")
              lib.pausa("cyan","Digite <Enter> paa continuar...")


