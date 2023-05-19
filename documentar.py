#Docstring
#__doc__ (modulos,clases,metodos, funciones)

def suma(numero1,numero2):
    '''
    La funcion suma 2 numeros enteros.
    
    Argumentos:
    numero1 (int)
    numero2 (int)

    Se retorna la suma de los parametros
    '''


    return numero1 + numero2

#print(suma.__doc__)
print(help(suma))
#ambas lineas devuelven lo mismo.

