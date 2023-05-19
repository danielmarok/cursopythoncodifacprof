#USO DE PARAMETROS EN DECORADORES
def funcion_a(funcion_b):#FUNCION B es la funcion a decorar

    def funcion_c(*args,**kwargs):#es la funcion decorada, encargada de extender la funcion principal a decorar
        print('-->Antes del llamado a la funcion b')
        resultado = funcion_b(*args,**kwargs)
        print('despues del llamado a la funcion b')

        return resultado
        
    return funcion_c

@funcion_a
def suma(numero1,numero2):
    return numero1 + numero2

resultado = suma(10,30)
print(resultado)
