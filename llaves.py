diccionario = {'a':1,'b':2,'c':3,'d':4}
#keys , values , items

llaves = diccionario.keys()
print(llaves)
#lo convertimos a tupla
llaves2 = tuple(diccionario.keys())
print(llaves2)

valores = tuple(diccionario.values())
print(valores)

elementos = diccionario.items()
#mejor siempre pasarlos a tuplas. elementos = tuple(diccionaro.items())
print(elementos)


