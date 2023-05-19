class Usuario:
    #__init__ :python maneja internamente este metodo init,mediante este metodo se podra 

    #Object
    def __init__(self,username='',password=''):#init se llama cuando instanciemos un objeto
        self.username = username
        self.password = password


user1 = Usuario('User1','pass1')
user2 = Usuario('User2','pass2')
user3 = Usuario('User3','pass3')
user4 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)

