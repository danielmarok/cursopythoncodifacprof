promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >=7

# print(promedio(10,4,5,6,7))
# print(aprobatorio(4))
def es_aprobatorio(calificacion):
    return calificacion >=9


def mostrar_mensaje(func_promedio,func_aprobatorio,*args):
    promedio = func_promedio(*args)#para pasar la N cantidad de argumentos a esta func_promedio
    #tengo poner el *args

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con: {promedio}.')
    else:
        print(f'Tu nota {promedio} no alcanzo para aprobar la materia')


# mostrar_mensaje(promedio,aprobatorio,10,5,2,7,7)
mostrar_mensaje(promedio,es_aprobatorio,10,10,8,9,9)
