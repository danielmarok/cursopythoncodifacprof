#primer ejemplo
""" def funcion_principal():
    a='a'  #variable locales,pero,son alcanzadas o utilizadas por bloques inferiores.Tienen Scope Alto.
    b='b'

    def funcion_anidada():
        c='c' #variable local
#si aca coloco una variable b, no es el mismo b que funcion_principal, son distintos,
#estan en diferentes scope.
        print(a)
        print(b)


    funcion_anidada()
    # print(c)


funcion_principal()
#nos da error porque en la linea 14 print(c) ,la variable c es desconocida para funcion principal.
#si uso una variable global, puede ser usada en cualquier parte del programa.
 """
e = 'e'#variable global
def funcion_principal():
    a='a'  #variable locales,pero,son alcanzadas o utilizadas por bloques inferiores.Tienen Scope Alto.
    b='b'

    def funcion_anidada():
        c='c' #variable local
        nonlocal b # si saco el nonlocal b ,van a tener distinto id las variables b
        b = 'cambio de valor '

        print(a)
        print(b)
        print(id(b))

        print(e)


    funcion_anidada()
    print(b)
    print(id(b))


funcion_principal()
