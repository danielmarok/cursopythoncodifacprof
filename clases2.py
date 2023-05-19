#Attrs clase
#Attrs instancia

class Usuario:
    username = 'Username por default'
    email = ''

Usuario.username = 'User dani'
Usuario.email = 'dam.@gmail'

print(Usuario.username,'---',Usuario.email)
