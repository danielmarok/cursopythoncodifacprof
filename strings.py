lenguajes = 'Python Ruby Java Rust C++ C'
listado_lenguajes = lenguajes.split()#separa por espacio nomas
#listado_lenguajes = lenguajes.split(' ',2) , separa por espacio y divide hasta 2, osea tendre tres elementos
#tres elementos 0,1,2
#el split divide por un espacio, si pongo - (guion) los toma como uno
#si pongo lenguajes.split('-') , divide mediante guiones
print(listado_lenguajes)

print('-------------------0--------------LISTADO A STRING')

lenguajess = ['Python','Ruby','Java','Rust']

string_lenguajes = ' '.join(lenguajess)
#string_lenguajes = '.'.join(lenguajess) -en este caso les pone punto
print(string_lenguajes)

