calificacion = 5
color = None
'''
if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion,color)
'''

#TRANSFORMAMOS TODO A UNA SOLA LINEA DE CODIGO
color = 'Verde' if calificacion >=7 else 'Rojo'

print(calificacion,color)

