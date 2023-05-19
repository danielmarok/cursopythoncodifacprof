lista =[1,2,3,4,5]
tupla = (10,20,30,40,50)

resultado = zip(tupla,lista)
#NOTA SI PONGO PRIMERO ESPACIO Y LUEGO UNA LINEA DE CODIGO ME MARCA ERROR!!!
print(resultado)
#me crea un objeto de tipo zip
print('-----------0--------------')
#si hago
resultado = tuple(resultado)#puedo usar list(), pero lo aconsejable es usar tuplas 
print(resultado)
#imprime la tupla en conjunto con la lista
#y si cambio en resultado = zip(lista,tupla) , los devuelve al reves

print('---------0--------PRIMER PAREJA')
primer_pareja = resultado[0]
print(primer_pareja)

