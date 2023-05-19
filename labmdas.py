def centigrados_a_farhenheit(grados):
    return grados * 1.8 +32


mi_funcion = centigrados_a_farhenheit
#mi_funcion = centigrados_a_farhenheit()  SI PONGO PARENTESIS ESTOY LLAMANDO A LA FUNCION. MAL

print(type(mi_funcion))
print(mi_funcion(10))
