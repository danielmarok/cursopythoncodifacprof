numeros = (1,2,3,4)

#primera forma
#uno,dos,tres,cuatro = 1,2,3,4 

#segunda forma usando tupla
uno,dos,tres,cuatro = numeros #otra forma de usar tupla
#si pongo un valor mas a la tupla Y NO le asigno una variable, da error

print(uno)
print(dos)
print(tres)
print(cuatro)

print('------------0---------------')
#poner el resto de valores de otra forma
numeros_2 =(6,7,8,9,10,11,12)

seis,siete,ocho,*losdemas = numeros_2
#python es inteligente para saber el resto de valores no se les asigno variables
#si en la declaracion de variables pongo *_ --> seis,siete,ocho,*_ 
#le estoy diciendo a python que no trabajo con el resto de valaores, le digo que omita valores
#si en cambio quiero omitir el 8,9,10 pondria-->seis,siete,*_,once,doce = numeros_2
#seis, _, ocho, *resto = numeros_2 -->le digo que el siete no lo cuente.. para eso el guion bajo.

print(seis)
print(siete)
print(ocho)
print(losdemas)

