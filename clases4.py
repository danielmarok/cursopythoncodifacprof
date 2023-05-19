
class Usuario:
    #Attrs de clase
    username = 'Username por default'
    email = 'dam@gmail.com'

#__dict__

user1 = Usuario()
user2 = Usuario()
user1.username = 'Cody'
#añado un nuevo atributo al objeto user1
user1.password = '1234'
#a diferencia de otros lenguajes no necesite declarar el nuevo atributo, es bueno pero daña legibilidad
user2.correo = 'dani@laplata'

print(user1.username)
# print(user2.password) -ERROR PORQUE el attr password no pertenece al objeto user1

print(id(user1.username))
print(id(Usuario.username))
#ahora me va a dar con IDs diferentes, porque al objeto user1 le cambie valor al atributo username.

print(user2.correo)

print(user1.__dict__)#Dict
print(user2.__dict__)#Dict

#ahora el diccionario no esta vacio porque el objeto tiene atributos
#dentro del diccionario se encuentra un item ahora. Una llave y un valor
