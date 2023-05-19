lista = [8,90,1,5,44,132,600,3,4]

lista_ordenada = list()
lista_ordenada = lista[:]

lista_ordenada.sort()#ordena forma ascendente
#de forma descendente lista_ordenada(sort(reverse=True))

print(lista_ordenada)
print(lista)
print('-------------0------------')
#forma descendente
lista_ordenada.sort(reverse=True)
print(lista_ordenada)

#funcion min y funcion max
print('-------------0------------')
print(min(lista))
print(max(lista))

#saber si un elemento se encuentra en la lista
print('-------------0------------')
print(10 in lista)

buscar = 10 not in lista
print(buscar)

#buscar indice
print('-------------0------------')
#devuelve el indice donde se encuentra el elemento
index = lista.index(5)
index2 = lista_ordenada.index(5)
#si tenemos mas 5, me devuelve el primero que encuentra, osea si tengo tres veces 5.
#si usamos index y el elemento no se encuentra da error y para el programa. Primero debemos verificar
#que se encuentra el elemento
print(index)
print(index2)


