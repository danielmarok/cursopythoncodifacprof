
#Indices     0     1   2    3     4      5
tupla = ('String',10,15.4,True,[1,2,3],(4,5,6))

print(tupla)

print('-------------------0------------------')

cursos = ('Python','Django','Flask','Rails','MongoDB')
#Indices      0        1       2       3       4

primer_curso = cursos[0]
ultimo_curso = cursos[-1]
print(primer_curso)
print(ultimo_curso)

#sub tuplas
print('-------------------0--------SUBTUPLAS----------')
sub_tuplas = cursos[0:3] #trabaja igual que con las listas, tambien con saltos
#va a tomar en realidad desde el indice cero, hasta el 2. El elemento en el indice 3 no lo tiene en cuenta
print(sub_tuplas)

#Listas y Tuplas
print('-------------0---------Listas y tuplas------')

cursos = ['Python','Django','Flask']

#convertir lista a tupla
cursos_tupla = tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))

niveles = ('Basico','Intermedio','Avanzado')

#convertir tupla a lista
niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))


