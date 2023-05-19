contador = 1

while contador <= 10:
    print(contador)

    contador +=1

print('--------0----------CONTADOR DIGITOS')

numero = 123456789356367468474
contador_digitos = 0

while numero >= 1:
    contador_digitos+=1

    numero = numero / 10
else:
    print('Fin del ciclo while')

print('El numero posee',contador_digitos,' digitos')

