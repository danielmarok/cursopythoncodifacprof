diccionario = {'a':1,'b':2,'c':3,'d':4}

print('z' in diccionario)

valor = diccionario['a']
#si pongo una llave que no existe da error.

print(valor)
print(diccionario)

print('---------0-------METODO GET')
#valor = diccionario.get('z')
valor = diccionario.get('z','La llave no existe en el diccionario')
#si uso un argumento mas coloco un mensaje u otro valor, por default devuelve None
print(valor)
#Obtenemos None, nos dice la ausencia de un valor..con get no nos da una excepcion o error

print('--------0-------METODO SET')
valor = diccionario.setdefault('e',5)
#setdefault lo que hace es que en caso de que no exista, lo agrega
print(valor)
print(diccionario)







