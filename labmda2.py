#labmda <parametros> : <cuerpo de la funcion>

funcion_grados = lambda grados : grados * 1.8 +32

print(funcion_grados(10))
print(type(funcion_grados))

'''
sin_parametros = lambda : True
parametros_default = lambda p1=10,p2=20,p3=30 : p1 + p2 + p3
asterisco = lambda *args,**kwargs : len(args) + len(kwargs)

'''