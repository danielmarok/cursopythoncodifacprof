class Animal():

    def comer(self):
        print('El animal come')
    
    def dormir(self):
        print('El animal duerme')


class Mascota(Animal):#clase padre
    pass


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota,Felino):#Clase hija
    pass

tutuca = Gato()
tutuca.comer()
tutuca.dormir()
tutuca.cazar()
