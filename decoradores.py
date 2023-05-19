#
'''
a -> la funcion principal(decorador)
b -> la funcion decorar
c -> la funcion decorada

a(b) -> c
'''
def funcion_a(funcion_b):#funcion a decorar
    print('@@HOLA SOY FUNCION A@@@')

    def funcion_c():#funcion decorada
        # funcion_b con solo esta linea no devuelve nada porque funcion_b seria una variable local,faltan
        #parentesis
        print('-->Antes del llamado a la funcion b')
        funcion_b()#SOY LA FUNCION REUTILIZABLE o decorada..
        print('despues del llamado a la funcion b')

        
    return funcion_c
# print('@@HOLA SOY FUNCION A@@') ->ESTA AFUERA DE LA FUNCION A

@funcion_a
def saludar():
    print('Hola nos encontramos en una funcion')    


saludar()

print('--------0--------REUTILIZANDO MISMO DECORADOR')

@funcion_a
def suma():
    print(10+30)

suma()

