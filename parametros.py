def area_circulo (radio,pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(10)
#resultado = area_circulo(radio=10,pi=3.1415926535) es valido tambien
#resultado = area_circulo(10,3.141592) igual puedo asignar valor al parametro pi
print(resultado)

