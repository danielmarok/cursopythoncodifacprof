#Attrs clase
#Attrs instancia

class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = 'dam@gmail.com'

#__dict__

user1 = Usuario()
#Pasos de verificacion de attr:
#1- verifica si el attr existen dentro del objeto
#2-Verifica si el atributo existe dentro de la clase,si existe lo utiliza, ES LO QUE PASA EN ESTE EJEMPLO
#solo lo puede usar para lectura
#3- Lanzar error
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))
#como usamos el mismo atributo, debe ser el mismo ID    

print(user1.__dict__)#Dict
#almacena en un diccionario todos los atributos que posea nuestro objeto
