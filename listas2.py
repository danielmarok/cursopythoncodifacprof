lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

lista_cursos.append('MongoDB')
print(lista_cursos)
print(len(lista_cursos))
lista_cursos.insert(1, 'Rails')
print(lista_cursos)

#ahora quiero agregar mi lista cursos 2 a lista cursos , uso metodo extend
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)

#eliminar elementos de la lista, metodo remove
lista_cursos.remove('MongoDB')
print(lista_cursos)

#ahora usando indices
print('---------------------0------------------------')
del lista_cursos[0]
#si quiero eliminar el ultimo elemento pondria -1 (en vez de contar si es que desconozco la lista)
print(lista_cursos)

#metodo clear -->lista_cursos.clear() , borra todos los elementos de la lista



