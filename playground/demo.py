dormido = True
cafe = 0

while dormido == True:
    print('toma un café')
    cafe += 1
    print(f'llevas {cafe} cafés')
    respuesta = input('Ya despertaste? s/n')
    if respuesta == 's':
        print('ya no necesitas más café')
        print(f'en total tomaste {cafe} tazas de café')
        break
    else:
        print('toma otra taza de café')

