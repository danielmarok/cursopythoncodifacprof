animal = 'Leon'# variable global ->puedo usar en funcion,condicion,ciclos

def imprimir_animal():
    """ global animal
    animal = 'Ballena' """#con estas dos linesa modifico y uso la variable global animal, y van a tener mismo id
    animal = 'Ballena' #variable local
    print(animal)
    print(id(animal))

#ambas variables con mismo nombre tienen diferentes Scope o alcance.

imprimir_animal()
print(animal)
print(id(animal))
