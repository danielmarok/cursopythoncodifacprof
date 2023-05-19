def suma(n1, n2):
    return n1 + n2 #sin usar resultado.. que era una linea demas.

#     resultado = n1 + n2    
#     return resultado
#ahora usando return

numero_uno = int(input('Ingrese el primer numero entero: '))
numero_dos = int(input('Ingrese el segundo numero entero: '))

resultado = suma(numero_uno,numero_dos)
print(resultado)


""" EJEMPLO USANDO PARAMETROS
def suma(n1, n2):
     resultado = n1 + n2
     print(resultado)


numero_uno = int(input('Ingrese el primer numero entero: '))
numero_dos = int(input('Ingrese el segundo numero entero: '))

suma(numero_uno,numero_dos)
 """

""" EJEMPLO SIN PARAMETROS
def suma():
    numero_uno = int(input('Ingrese el primer numero entero: '))
    numero_dos = int(input('Ingrese el segundo nro entero: '))

    resultado = numero_uno + numero_dos
    print(resultado)

suma()
 """
