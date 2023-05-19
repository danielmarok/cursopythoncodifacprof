def promedio(*args):#Tupla argumento
    return sum(args) / len(args)


def usuarios(**kwargs):#Diccionario parametro
    print(kwargs)
    print(type(kwargs))
#**kwargs es un diccionario como parametros

usuarios(eduardo=[10,10,8],fernando=[10,9,9])
#eduardo es la key, la lista son los valores

print('-----------0-------------COMBINACION')

def combinacion(*args,**kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

diccio={'codi':True,'curso':'Python'}

#combinacion(1,2,3,4,5,cody=True,curso='Python')
combinacion(1,2,3,4,5,diccio)

