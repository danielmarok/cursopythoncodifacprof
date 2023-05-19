class Usuario:
    #__init__ :python maneja internamente este metodo init,mediante este metodo se podra 
    #inicializar objetos.Dice que no hace falta hacer la funcion inicializar, es repetitivo
    #pero es buen ejemplo.


    def inicializar(self,username,password):#mediante este metodo seremos capaces de inicializar los attr de nuestros objetos
        #por convencion el parametro se llamara self.
        self.username = username
        self.password = password
        #estos attr se añaden a los objetos


user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1','pass1')
user2.inicializar('user2','pass2')

print(user1.__dict__)
print(user2.__dict__)

