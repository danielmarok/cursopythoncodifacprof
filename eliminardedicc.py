diccionario = {'a':1,'b':2,'c':3,'d':4}
del diccionario ['a']
valor = diccionario.pop('b')
#pop devuelve el valor de la llave que se borro
#usando del y pop, si colocamos llaves inexistente nos da KeyEror
print(diccionario)
print(valor)

diccionario.clear()
print(diccionario)

