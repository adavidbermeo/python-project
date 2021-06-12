isRegistered = True
print(type(isRegistered))

while (isRegistered):
  print('Esta registrado')
  isRegistered = input('Sigue estando registrado (Si/No): ')
  if (isRegistered != 'Si'):
    isRegistered = False