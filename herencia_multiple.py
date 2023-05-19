class Mascota:#clase padre
    
    def comer(self):
        print('la mascota come')
    
    def dormir(self):
        print('la mascota duerme')

class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota,Felino):#Clase hija
    pass #Si no pongo el PASS me da error y no deja guardar, menos va andar.
         # me exige que ponga algo en el cuerpo de la funcion y puedo poner pass para resolver esto.

tutuca = Gato()
tutuca.comer()
tutuca.dormir()
tutuca.cazar()
