#lista = list()
#otra forma de declarar listas
#Indices    0       1   2     3    4  5  6
lista = ['String', 10, 15.6, True, 4, 5, 6]
#Leer lista de derecha a izquierda lista(-1)= True, lista(-2)= 15.6, etc..
#primer elemento lista[0]
#ejemplo de reemplazar elemento lista
lista[3] = False

print(lista)
#crear sublista
sub_lista = lista[0:3] #el elemento 3 no se incluye a la sub lista
#sub_lista contiene->String, 10,15.6 
#NO CUENTA EL INDICE 3 COMO ELEMENTO, el indice final no es tomado en cuenta.

print("Sublista:  ",sub_lista)


#mejor declarar listas de un solo tipo
lista_strings = ["daniel", "angel", "kensai"]
lista_enteros = [0, 1, 2, 3, 4]
lista_floats = [19.5, 4.5, 3.45, 6.678]
lista_booleanos = [True, False, (2<10), (4>3 and 10 !=11)]

print (lista_booleanos)

