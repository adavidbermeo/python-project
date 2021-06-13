# Seguimos trabajando con el condicional IF. ahora vemos las instrucciones else y elif.

edad_usuario = int(input('Ingese su edad, por favor: '))

if edad_usuario < 18:
    print('Puede ingresar')
elif edad_usuario > 100:
    print('Edad incorrecta')
else:
    print('No puede ingresar')
print('El programa finalizo')
