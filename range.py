
""" rango = range(11)#0-10 , range comienza del 0 y el 11 no se encuentra dentro del rango
print(rango)
print(type(rango))
 """

""" for valor in rango:
    print(valor) """
#pero son 11 iteraciones, A TENER EN CUENTA

#AHORA COLOCANDO ARGUMENTOS
""" for valor in range(5,21,2):
    print(valor)
 """#dos argumentos, el primero dice desde donde inicia
#tercer argumento me dice los saltos.
#-------------0---------FUNCION ENUMERATE

numeros = [10,20,30,40,50]
cadena = 'Prueba con String'

for indice,elemento in enumerate(numeros,10):
    print(indice,elemento)
#puse un string y funka igual
#si coloco el argumento 10, comienza el indice desde 10


