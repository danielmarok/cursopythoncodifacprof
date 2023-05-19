def promedio (*args):
    return sum (args) / len (args)


def combinacion(p1,p2,*args,p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

    
#p4 es un parametro opcional que DEBE encontrarse a la derecha de *args
combinacion(10,20,1,2,4,5,6,7,8)
#args los toma como tuplas


""" def promedio(*args):
    print(args)
    print(type(args))

    return sum(args) / len (args)
#estamos usando args, que es un tipo de argumento que representa un conjunto de valores que ingresaran
#por convecion de la comunidad python, se usa *args , siempre se escriben asi.
resultado = promedio(10,10,5,7,10)
print(resultado)
 """
""" 
def promedio(listado):
    return sum (listado) / len(listado)


resultado = promedio ([10,10,5,7,10])
print(resultado) """